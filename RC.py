from machine import Pin, ADC
import time
import network
import espnow
import neopixel

# Initialize ESP-NOW
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(0.5)
esp = espnow.ESPNow()
esp.active(True)

# Device MAC Addresses (Replace with actual MACs)
device_macs = [
    b'...',  # Device 1 MAC Address
    b'...',  # Device 2 MAC Address
    b'...'   # Device 3 MAC Address
]

# Register all devices as peers
for mac in device_macs:
    esp.add_peer(mac)

# Onboard NeoPixel LED
NEOPIXEL_PIN = 8  # Onboard LED for ESP32-C6
np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), 1)

def set_led_color(color):
    """Set onboard NeoPixel color."""
    np[0] = color
    np.write()

# Joystick Pins
joy1_x = ADC(Pin(2))
joy1_y = ADC(Pin(3))
joy2_x = ADC(Pin(0))
joy2_y = ADC(Pin(1))

# Set ADC to 12-bit
for joy in [joy1_x, joy1_y, joy2_x, joy2_y]:
    joy.atten(ADC.ATTN_11DB)

# Joystick Buttons
joy1_sw = Pin(4, Pin.IN, Pin.PULL_UP)   # Joystick 1 Button
joy2_sw = Pin(5, Pin.IN, Pin.PULL_UP)  # Joystick 2 Button

# Other Buttons
buttons = [
    Pin(15, Pin.IN, Pin.PULL_DOWN),  # Device Switch (Button 1)
    Pin(21, Pin.IN, Pin.PULL_DOWN),  # Button 2
    Pin(22, Pin.IN, Pin.PULL_DOWN),  # Button 3
    Pin(19, Pin.IN, Pin.PULL_DOWN),  # Button 4
]

# Device Selection Variables
active_device = 0  # 0 = Device 1, 1 = Device 2, 2 = Device 3
last_button1_state = 0

def switch_device():
    """Cycle through devices and update onboard LED color."""
    global active_device
    active_device = (active_device + 1) % 3  # Cycle 0 → 1 → 2 → 0
    
    # Set onboard LED color
    if active_device == 0:
        set_led_color((10, 0, 0))  # Green for Device 1
    elif active_device == 1:
        set_led_color((0, 10, 0))  # Red for Device 2
    elif active_device == 2:
        set_led_color((0, 0, 10))  # Blue for Device 3

# Set initial LED color
switch_device()

while True:
    # Check Button 1 for device switching
    button1_state = buttons[0].value()
    if button1_state and not last_button1_state:
        switch_device()  # Change device
        time.sleep(0.2)  # Debounce

    last_button1_state = button1_state

    # Read joystick values
    joystick_data = {
        "Joystick1-X": joy1_x.read(),
        "Joystick1-Y": joy1_y.read(),
        "Joystick2-X": joy2_x.read(),
        "Joystick2-Y": joy2_y.read(),
    }

    # Read joystick button states
    joystick_button_data = {
        "Joystick1-Button": joy1_sw.value(),
        "Joystick2-Button": joy2_sw.value(),
    }

    # Read button states
    button_data = {f"Button{i+1}": btn.value() for i, btn in enumerate(buttons)}

    # Merge data correctly
    data = joystick_data.copy()  # Copy joystick data
    data.update(joystick_button_data)  # Add joystick button states
    data.update(button_data)  # Merge other button states
    data["Device"] = active_device  # Add active device info

    # Send data only to the active device
    esp.send(device_macs[active_device], bytes(str(data), 'utf-8'))  # Convert to bytes

    print(f"Sent to Device {active_device+1}: {data}")
    time.sleep(0.07)


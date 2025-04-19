# 🎮 ESP-Now RC Controller

A powerful and flexible remote control system built with MicroPython, using ESP-NOW protocol for wireless communication. This project allows you to control multiple devices wirelessly using a custom-built controller with dual joysticks and multiple buttons.

## ✨ Features

- **Wireless Communication**: Uses ESP-NOW protocol for fast and reliable wireless communication
- **Multi-Device Support**: Control up to 3 or more different devices with a single controller
- **Dual Joystick Control**: Two analog joysticks for precise control
- **Multiple Buttons**: 4 additional programmable buttons
- **Visual Feedback**: Onboard NeoPixel LED for device selection feedback
- **Real-time Data Transmission**: Low-latency communication between controller and devices

## 🛠️ Hardware Requirements

- ESP32-C6 microcontroller
- 2x Analog Joysticks
- 4x Push Buttons
- NeoPixel LED
- Power supply (battery or USB)

## 📋 Pin Configuration

| Component | Pin |
|-----------|-----|
| Joystick 1 X-Axis | GPIO 2 |
| Joystick 1 Y-Axis | GPIO 3 |
| Joystick 2 X-Axis | GPIO 0 |
| Joystick 2 Y-Axis | GPIO 1 |
| Joystick 1 Button | GPIO 4 |
| Joystick 2 Button | GPIO 5 |
| Device Switch | GPIO 15 |
| Button 2 | GPIO 21 |
| Button 3 | GPIO 22 |
| Button 4 | GPIO 19 |
| NeoPixel LED | GPIO 8 |

## 🚀 Getting Started

1. **Hardware Setup**
   - Connect the joysticks and buttons according to the pin configuration
   - Ensure proper power supply to the ESP32-C6

2. **Software Setup**
   - Flash MicroPython to your ESP32-C6
   - Upload the `RC.py` file to your device
   - Configure the MAC addresses of your target devices

3. **Usage**
   - Power on the controller
   - Use Button 1 to switch between devices
   - The NeoPixel LED will indicate the currently selected device:
     - Green: Device 1
     - Red: Device 2
     - Blue: Device 3

## 🔧 Configuration

To configure the MAC addresses of your target devices, modify the `device_macs` list in `RC.py`:

```python
device_macs = [
    b'...',  # Device 1 MAC Address
    b'...',  # Device 2 MAC Address
    b'...'   # Device 3 MAC Address
]
```

## 📦 Data Format

The controller sends data in the following format:

```json
{
    "Joystick1-X": value,
    "Joystick1-Y": value,
    "Joystick2-X": value,
    "Joystick2-Y": value,
    "Joystick1-Button": value,
    "Joystick2-Button": value,
    "Button1": value,
    "Button2": value,
    "Button3": value,
    "Button4": value,
    "Device": active_device_index
}
```

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. ESP-NOW Connection Issues
- **Problem**: Devices not connecting or communication failing
- **Solution**:
  - Ensure all devices are powered on
  - Verify MAC addresses are correctly configured
  - Check if devices are within range (typically 100-200 meters in open space)
  - Try resetting both the controller and receiver devices

#### 2. Joystick Calibration Issues
- **Problem**: Joystick values not centered or not responding correctly
- **Solution**:
  - Check if joysticks are properly connected to the correct GPIO pins
  - Verify ADC attenuation settings (should be set to 11DB)
  - Test joystick values using a simple print statement in the code
  - Ensure joysticks are properly powered (3.3V)

#### 3. Button Response Problems
- **Problem**: Buttons not responding or triggering multiple times
- **Solution**:
  - Check button connections and pull-up/down resistors
  - Verify GPIO pin configurations
  - Add debounce delay if buttons are triggering multiple times
  - Test button states using a simple print statement

#### 4. NeoPixel LED Issues
- **Problem**: LED not lighting up or showing wrong colors
- **Solution**:
  - Verify NeoPixel connection (data pin and power)
  - Check if the correct number of LEDs is configured
  - Ensure proper power supply (5V recommended for NeoPixels)
  - Test LED with a simple color test function

#### 5. Power Issues
- **Problem**: Device resetting or behaving erratically
- **Solution**:
  - Check power supply voltage (should be stable 3.3V)
  - Ensure sufficient current capacity (ESP32-C6 can draw up to 500mA)
  - Add decoupling capacitors near the power pins
  - Consider using a separate power supply for NeoPixels

#### 6. MicroPython Issues
- **Problem**: Code not running or errors in execution
- **Solution**:
  - Verify MicroPython version compatibility
  - Check if all required modules are installed
  - Ensure proper file upload to the device
  - Try resetting the device and re-uploading the code

### Debugging Tips
1. Use the REPL (Read-Eval-Print Loop) to test individual components
2. Add print statements to monitor data flow
3. Check the serial monitor for error messages
4. Test components individually before full integration
5. Keep a backup of working code versions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MicroPython team for the amazing firmware
- ESP-NOW protocol for reliable wireless communication
- The open-source community for inspiration and support
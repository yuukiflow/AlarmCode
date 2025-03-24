# Raspberry Pi LED Control System

A collection of Python scripts for controlling RGB LED strips connected to a Raspberry Pi. This project provides various lighting effects and control methods for RGB LED strips using PWM (Pulse Width Modulation).

## Features

- RGB LED strip control with PWM
- Multiple lighting effects:
  - Fading color transitions
  - Strobe effects
  - Pulse effects
  - Dawn simulation (alarm)
  - Dimming control
- Button-triggered light control
- Real-time brightness adjustment

## Hardware Requirements

- Raspberry Pi (any model with GPIO pins)
- RGB LED strip
- 3 GPIO pins for RGB control (configurable)
- Optional: Push button for trigger control

## Pin Configuration

Default GPIO pin configuration:
- Red LED: GPIO 17
- Green LED: GPIO 22
- Blue LED: GPIO 24
- Button Input: GPIO 13 (if using trigger control)

## Available Scripts

- `LED_strip.py`: Basic RGB LED control
- `fading.py`: Smooth color transition effects
- `strobo.py`: Strobe light effect
- `pulse.py`: Pulsing light effect
- `dim.py`: Brightness control
- `LightTrigger.py`: Button-controlled light switching
- `LightPress.py`: Interactive button control
- `reveil_aube.py`: Dawn simulation alarm

## Dependencies

- RPi.GPIO
- pigpio
- Python 2.7 or 3.x

## Usage

1. Connect your RGB LED strip to the specified GPIO pins
2. Install required dependencies
3. Run any of the available scripts:
   ```bash
   python3 script_name.py
   ```

## Controls

When using interactive scripts:
- `+` / `-`: Increase / Decrease brightness
- `p` / `r`: Pause / Resume effects
- `c`: Abort program

## Notes

- Ensure proper power supply for your LED strip
- Some scripts require root privileges to access GPIO
- Always use appropriate resistors if needed for your LED strip

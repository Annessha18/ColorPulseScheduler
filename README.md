# ColorPulseScheduler
ColorPulseScheduler is a Python script designed to control a WS2812B LED strip connected to a Raspberry Pi. The script changes the color of the LEDs in a timed cycle every 5 minutes, rotating through a series of colors: orange, green, red, yellow, and blue. Perfect for ambient lighting projects or visual notifications.

Features
- Cycles through five colors: Orange, Green, Red, Yellow, and Blue.
- Changes color every 5 minutes.
- Easy setup and customizable LED configurations.
- Automatically turns off LEDs on exit.

Requirements
Hardware: 
   - Raspberry Pi
   - WS2812B LED strip (or similar NeoPixel-compatible LEDs)
Software:
   - Python 3
   - `rpi_ws281x` and `adafruit-circuitpython-neopixel` libraries

Installation
Install the required Python libraries:
   ```bash
   pip install rpi_ws281x adafruit-circuitpython-neopixel

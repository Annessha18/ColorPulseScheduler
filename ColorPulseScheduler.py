import time
import board
import neopixel

# Set up your LED strip
LED_PIN = board.D18  # Pin connected to the data input of the LED strip
NUM_LEDS = 30        # Number of LEDs in your strip
BRIGHTNESS = 0.5     # Brightness level (0.0 to 1.0)
DELAY = 300          # Delay time in seconds (5 minutes)

# Define colors (R, G, B)
colors = [
    (255, 165, 0),   # Orange
    (0, 255, 0),     # Green
    (255, 0, 0),     # Red
    (255, 255, 0),   # Yellow
    (0, 0, 255)      # Blue
]

# Initialize the LED strip
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

def change_color(color):
    for i in range(NUM_LEDS):
        pixels[i] = color
    pixels.show()

try:
    color_index = 0
    while True:
        change_color(colors[color_index])       # Set the color
        color_index = (color_index + 1) % len(colors)  # Move to the next color in the list
        time.sleep(DELAY)                       # Wait 5 minutes before changing color

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))  # Turn off all LEDs on exit
    pixels.show()

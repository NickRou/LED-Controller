from neopixel import *
import re
from matplotlib import colors
import time

class LED:
    LED_COUNT = 160
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_INVERT = False
    LED_BRIGHTNESS = 150
    LED_CHANNEL = 0

    def __init__(self):
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA,
                                       self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        self.strip.begin()

    def colorWipe(self, color):
        """Wipe color across display a pixel at a time."""
        g, r, b = self.getRGB(color)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(g, r, b))
            self.strip.show()

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.LED_COUNT):
                self.strip.setPixelColor(i, self.wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.LED_COUNT):
                self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.LED_COUNT) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def getRGB(self, color):
        re.sub('[A-Za-z]+', '', color)
        color = color.lower()
        r, g, b = colors.to_rgb(color)
        return (int) (g * 255), (int) (r * 255), (int) (b * 255)
    
    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
        
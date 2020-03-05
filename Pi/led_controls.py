from neopixel import *
import re

class LED:
    LED_COUNT = 78
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
        r, g, b = self.getRGB(color)
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
            self.strip.show()

    def getRGB(self, color):
        re.sub('[A-Za-z]+', '', color)
        color = color.lower()
        if color == 'orange':
            return 255, 165, 0
        elif color == 'red':
            return 255, 0, 0
        elif color == 'green':
            return 0, 255, 0
        elif color =='blue':
            return 0, 0, 255
        else:
            print("RGB for this color not recorded. Setting to default.")
            return 255, 165, 0
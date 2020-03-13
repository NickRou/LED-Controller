from neopixel import *
from ast import literal_eval as make_tuple
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

    def colorWipe(self, rgbString):
        #Wipe color across display a pixel at a time.
        rgb = make_tuple(rgbString[3:])
        r, g, b = rgb[0], rgb[1], rgb[2]

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(g, r, b))
            self.strip.show()
        
    """
    TODO: Add options for animations on Flask app
    def rainbow(self, wait_ms=20, iterations=1):
        #Draw rainbow that fades across all pixels at once.
        for j in range(256*iterations):
            for i in range(self.LED_COUNT):
                self.strip.setPixelColor(i, self.wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        #Draw rainbow that uniformly distributes itself across all pixels.
        for j in range(256*iterations):
            for i in range(self.LED_COUNT):
                self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.LED_COUNT) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def wheel(self, pos):
        #Generate rainbow colors across 0-255 positions.
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
    """
    
    
    
        
import board
import neopixel


class LED:
    def __init__(self, pixel_pin, num_pixels, brightness, auto_write, order):
        self.pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness,
                                        auto_write=auto_write, pixel_order=order)

    def fill_color(self, rgb: tuple) -> None:
        self.pixels.fill(rgb)


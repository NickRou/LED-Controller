import speech_recognition as sr
import board
import neopixel

#LED settings
pixel_pin = board.D18
num_pixels = 78
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER)

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Say something!")
    audio = r.listen(source)
    
# recognize speech using Google Speech Recognition
try:
    statement = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said: " + statement)
    
    if "orange" in statement.lower():
        pixels.fill((64, 180, 0))
    elif "green" in statement.lower():
        pixels.fill((255, 0, 0))
    else:
        pixels.fill((0, 0, 0))
    pixels.show()
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

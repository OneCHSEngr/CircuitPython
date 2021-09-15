"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.3

print("This line will be printed.")

while True:
    led[0] = (255, 0, 0)
    print("RED")
    time.sleep(0.5)
    led[0] = (0, 255, 0)
    print("GREEN")
    time.sleep(0.5)
    print("BLUE")
    led[0] = (0, 0, 255)
    time.sleep(0.5)

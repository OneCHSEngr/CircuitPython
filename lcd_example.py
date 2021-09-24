# Working example of Dan Halbert's LCD code.
# https://github.com/dhalbert/CircuitPython_LCD
# I needed to create an i2c object and pass it to the interface
# added code to print ic2 address to serial monitor
# D. Dierolf 9/23/21

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from random import randint
import board
import time

print("running")

# get and i2c object
i2c = board.I2C()

while not i2c.try_lock():
    pass
print("I2C addresses found:", [hex(device_address)
              for device_address in i2c.scan()])
i2c.unlock()

# Talk to the LCD at I2C address 0x27
#     if error received -- ValueError: No I2C device at address: 0x3f
# try address 0x3f
# 16 columns, 2 rows, 8 pixels high characters

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_cols=16, num_rows=2, char_height=8)

lcd.print("abc ")
time.sleep(1)
lcd.print("This is quite long and will wrap onto the next line automatically.")
time.sleep(1)
lcd.clear()

while True:
    # jump around LCD screen
    lcd.clear()
    row = randint(0, 1)
    col = randint(0,15)
    lcd.set_cursor_pos(row, col)
    lcd.print("Here I am")
    time.sleep(.5)



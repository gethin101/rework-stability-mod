#circuit python
#COM -> GND
#NO -> GPIO 15

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

SWITCH_PIN = board.GP15    
DEBOUNCE_TIME = 0.15         


switch = digitalio.DigitalInOut(SWITCH_PIN)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP   

keyboard = Keyboard(usb_hid.devices)

last_state = switch.value
last_time = time.monotonic()

print("ready")

while True:
    current_state = switch.value
    now = time.monotonic()


    if current_state != last_state:
        last_state = current_state

        if not current_state and (now - last_time) > DEBOUNCE_TIME:
            print("taking photo")
            keyboard.press(Keycode.ENTER)
            keyboard.release_all()
            last_time = now

    time.sleep(0.005)


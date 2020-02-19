#import RPi.GPIO as GPIO
from gpiozero import LED, Button
import time

NULL_CHAR = chr(0)

switch1 = Button(23,pull_up=False)
led = LED(24)

last_state = switch1.is_pressed

def send_keys(keys):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(keys.encode())

def switch1_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(22) + NULL_CHAR*5
        led.on()
    else:
        print ("Switch off")
        #keys = NULL_CHAR*2 + chr(5) + NULL_CHAR*5
        keys = NULL_CHAR*8
        led.off()
    return(keys)



while True:

    # Switch 1
    current_state = switch1.is_pressed
    if current_state != last_state:
        #print("last state: %d" % last_state)
        last_state = current_state
        #print("state: %d" % current_state)
        keys = switch1_actions(current_state)
        send_keys(keys)

    time.sleep(0.01)


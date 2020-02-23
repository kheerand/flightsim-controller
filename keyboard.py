#import RPi.GPIO as GPIO
from gpiozero import LED, Button
import time

NULL_CHAR = chr(0)

switch1A = Button(13,pull_up=False)
switch2A = Button(19,pull_up=False)
switch3A = Button(26,pull_up=False)
switch4A = Button(17,pull_up=False)
switch5A = Button(27,pull_up=False)
switch6A = Button(22,pull_up=False)
switch6B = Button(10,pull_up=False)
switch7A = Button(9,pull_up=False)
switch7B = Button(11,pull_up=False)
switch8A = Button(5,pull_up=False)
switch8B = Button(6,pull_up=False)

def send_keys(keys,momentary=False):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(keys.encode())
        if momentary:
            fd.write((NULL_CHAR*8).encode())


####
# Switch actions
####
def switch1A_actions(state):
    if state == 0:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(22) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch2A_actions(state):
    if state == 0:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(23) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch3A_actions(state):
    if state == 0:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(24) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch4A_actions(state):
    if state == 0:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(26) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = chr(32)+NULL_CHAR + chr(26) + NULL_CHAR*5
    return(keys)

def switch5A_actions(state):
    if state == 0:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(20) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = chr(32)+NULL_CHAR + chr(20) + NULL_CHAR*5
    return(keys)


# Stuff up in how I wired it meant the switch logic is correct here
# but inverted in the SPST switches
def switch6A_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(47) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch6B_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(48) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch7A_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(38) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch7B_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(32) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch8A_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(31) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)

def switch8B_actions(state):
    if state == 1:
        print ("Switch pressed")
        keys = NULL_CHAR*2 + chr(32) + NULL_CHAR*5
    else:
        print ("Switch off")
        keys = NULL_CHAR*8
    return(keys)



# (switchID, momentary=True/False,action_function)
switch_list = [(switch1A,True,switch1A_actions),
               (switch2A,True,switch2A_actions),
               (switch3A,True,switch3A_actions),
               (switch4A,True,switch4A_actions),
               (switch5A,True,switch5A_actions),
               (switch6A,False,switch6A_actions),
               (switch6B,False,switch6B_actions),
               (switch7A,False,switch7A_actions),
               (switch7B,False,switch7B_actions),
               (switch8A,True,switch8A_actions),
               (switch8B,True,switch8B_actions)]


#=======
# END Switch actions
#=======

last_state = {}

# Init the last_state dictionary
for switch,*_ in switch_list:
    last_state[switch] = switch.is_pressed


while True:
    for switch,momentary,action in switch_list:
        current_state = switch.is_pressed
        if current_state != last_state[switch]:
            #print("last state: %d" % last_state)
            last_state[switch] = current_state
            #print("state: %d" % current_state)
            keys = action(current_state)
            send_keys(keys,momentary)

    time.sleep(0.01)


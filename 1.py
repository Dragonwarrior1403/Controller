#!/usr/bin/python
#sudo pip3 install evdev
from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event0')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            #print(keyevent.keycode[0])
            if keyevent.keycode[0] == 'B':
                print ("Back")
            elif keyevent.keycode[0] == 'BTN_A':
                print ("Forward")
            elif keyevent.keycode[0] == 'BTN_B':
                print ("Right")
            elif keyevent.keycode[0] == 'BTN_NORTH':
                print ("Left")
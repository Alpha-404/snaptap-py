import evdev
from evdev import InputDevice, categorize, ecodes

device = InputDevice('/dev/input/by-id/usb-SIGMACHIP_Trust_Keyboard-event-kbd')

"""""""""""
a_pressed = False
d_pressed = False
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        
        if key_event.keycode == 'KEY_A':
            if key_event.keystate == key_event.key_down:
                a_pressed = True
            elif key_event.keystate == key_event.key_up:
                a_pressed = False
        
        if key_event.keycode == 'KEY_D':
            if key_event.keystate == key_event.key_down:
                d_pressed = True
            elif key_event.keystate == key_event.key_up:
                d_pressed = False
        
        if key_event.keycode == 'KEY_A' and a_pressed:
            device.write(ecodes.EV_KEY, ecodes.KEY_D, 0)

        if key_event.keycode == 'KEY_D' and a_pressed:
            device.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
"""""""""""

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        
        if key_event.keycode == 'KEY_A' and key_event.keystate == key_event.key_down:
            device.write(ecodes.EV_KEY, ecodes.KEY_D, 0)

        if key_event.keycode == 'KEY_D' and key_event.keystate == key_event.key_down:
            device.write(ecodes.EV_KEY, ecodes.KEY_A, 0)
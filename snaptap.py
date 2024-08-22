import evdev
from evdev import InputDevice, categorize, ecodes

print("fyi you need to edit the code to put your keyboards input handle in the code")

device = InputDevice('/dev/input/by-id/usb-SIGMACHIP_Trust_Keyboard-event-kbd')

for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        key_event = categorize(event)
        
        if key_event.keycode == 'KEY_A' and key_event.keystate == key_event.key_down:
            device.write(ecodes.EV_KEY, ecodes.KEY_D, 0)

        if key_event.keycode == 'KEY_D' and key_event.keystate == key_event.key_down:
            device.write(ecodes.EV_KEY, ecodes.KEY_A, 0)

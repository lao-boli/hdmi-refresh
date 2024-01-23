import keyboard
import os

def hdmi():
    os.system('./hdmi.sh')


keyboard.add_hotkey('ctrl+shift+alt+1',hdmi)

while True:
    pass

from pynput import mouse
import sys

def wheel(on_scroll):
    return mouse.Listener(on_scroll=on_scroll)

sys.modules[__name__] = wheel
from pynput import mouse
import sys

position = {
    "x": 0,
    "y": 0,
    "dx": 0,
    "dy": 0
}

def on_scroll(x, y, dx, dy):
    global position
    position["x"] = x
    position["y"] = y
    position["dx"] = dx
    position["dy"] = dy

def wheel(on_scroll):
    return mouse.Listener(on_scroll=on_scroll)

def getWheel():
    global position
    return position

listener = wheel(on_scroll=on_scroll)
listener.start()
# listener.join()
from helpers import wheel

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

from helpers.webdriver import Browser

from helpers.tracker import EyeTracker
def main():
    # browser = Browser()

    # listener = wheel(on_scroll)
    # listener.start()
    # listener.join()
    eyeTracker = EyeTracker()
    while True:
        eyeTracker.analyze()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("stop")
        raise
from helpers import wheel
from helpers.webdriver import Browser
from helpers.tracker import EyeTracker
from helpers.excel import Excel
index = 0
path = "2021_08_16_18-21"

def main():
    global path

    browser = Browser()
    eyeTracker = EyeTracker()
    excel = Excel(path)

    def formatData(data, eyes):
        for eye in eyes:
            data.append(eye[0][0])
            data.append(eye[0][1])
            data.append(eye[1])


    def on_scroll(x, y, dx, dy):
        global index
        eyes = eyeTracker.analyze()
        if len(eyes) == 2:
            name = "screenshot-" + str(index)
            browser.toImg("./datasets/" + path + "/" + name)
            data = [name + ".png", x, y, dx, dy]
            formatData(data, eyes)
            excel.insert(data)
            print("Data : ", data)
            index += 1

    listener = wheel(on_scroll)
    listener.start()
    listener.join()


if __name__ == "__main__":
    main()
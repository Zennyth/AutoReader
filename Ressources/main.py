from helpers.wheel import getWheel
from helpers.webdriver import Browser
from helpers.tracker import EyeTracker
from helpers.excel import Excel


index = 0
path = "2021_08_17_12-00"

def main():
    global path

    browser = Browser()
    eyeTracker = EyeTracker()
    excel = Excel(path)

    def formatData(data, eyes):
        for eye in eyes:
            data.append(eye[0][0]) # eye's x position
            data.append(eye[0][1]) # eye's y position

    global index
    print("start")
    while True:
        eyes = eyeTracker.analyze()
        if len(eyes) == 2:
            name = "screenshot-" + str(index)
            #browser.toImg("./datasets/" + path + "/" + name)
            wheel = getWheel()
            data = [name + ".png", wheel["dx"], wheel["dy"]]
            formatData(data, eyes)
            excel.insert(data)
            print("Data : ", data)
            index += 1



if __name__ == "__main__":
    main()
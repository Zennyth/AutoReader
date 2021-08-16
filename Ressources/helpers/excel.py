from openpyxl import Workbook

class Excel:
    def __init__(self, folder):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.path = "./datasets/" + folder + "/wb.xlsx"
        self.folder = folder
        self.ws.append(["img", "x", "y", "dx", "dy", "leftEyeX", "leftEyeY", "leftEyeR", "rightEyeX", "rightEyeY", "rightEyeR"])
    
    def save(self):
        self.wb.save(self.path)

    def insert(self, data):
        self.ws.append(data)
        self.save()

    def __str__(self):
        return "Excel"
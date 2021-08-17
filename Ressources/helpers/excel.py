from openpyxl import Workbook
import csv

class Excel:
    def __init__(self, folder):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.path = "./datasets/" + folder + "/wb.xlsx"
        self.folder = folder
        self.ws.append(["img", "dx", "dy", "leftEyeX", "leftEyeY", "rightEyeX", "rightEyeY"])
    
    def save(self):
        self.wb.save(self.path)
        with open("./datasets/" + self.folder + "/wb.csv", 'w', newline="") as f:
            c = csv.writer(f)
            for r in self.ws.iter_rows(): # generator; was sh.rows
                c.writerow([cell.value for cell in r])

    def insert(self, data):
        self.ws.append(data)
        self.save()

    def __str__(self):
        return "Excel"
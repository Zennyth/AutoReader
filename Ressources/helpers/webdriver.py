from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

url = "https://readmanganato.com/manga-dg980989/chapter-116"

class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    
    def toImg(self, name):
        self.driver.save_screenshot(name + '.png')

    def __str__(self):
        return str(self.driver)
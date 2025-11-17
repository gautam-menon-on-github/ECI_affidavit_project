from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

class BaseScraper:
    def __init__(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)   # keeping it default at 10 seconds

    def quit(self):
        self.driver.quit()

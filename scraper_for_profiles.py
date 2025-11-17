from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

class ScraperForProfiles:

    def __init__(self):
        service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_profile(self, profile_url):
        self.driver.get(profile_url)

        # first scraping name and address.
        # through manual inspection, i found 7 divs with class="form-group"
        # out of which, number 3 and 5 are of importance since they have
        # the name and addresses within a div inside them.
        form_groups = self.driver.find_elements(By.CLASS_NAME, "form-group")
        candidate_name = form_groups[2].find_elements(By.TAG_NAME, 'p')[1].text
        address = form_groups[4].find_elements(By.TAG_NAME, 'p')[1].text

        # only gives the first result, which happens to be the download button for affidavit.
        affidavit_link = self.driver.find_element(By.TAG_NAME, 'button')
        affidavit_link.click()
        time.sleep(4)

        self.driver.close()

        # returns the name and address to be appended to the candidates_list
        return candidate_name, address
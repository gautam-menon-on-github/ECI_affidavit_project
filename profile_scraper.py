import time
from selenium.webdriver.common.by import By

class ProfileScraper:

    def __init__(self, driver):
        self.driver = driver

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

        # returns the name and address to be appended to the candidates_list
        return candidate_name, address

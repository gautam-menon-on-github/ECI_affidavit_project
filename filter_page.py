import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class FilterPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def apply_filters(self):
        self.driver.get('https://affidavit.eci.gov.in/')

        # the first dropdown: election type
        election_type = self.wait.until(
            EC.element_to_be_clickable((By.ID, "electionType"))
        )
        Select(election_type).select_by_value("27-AC-GENERAL-3-51")

        # waiting for elements in the next dropdown to be loaded
        time.sleep(2)

        # second dropdown: election
        election = self.wait.until(
            EC.element_to_be_clickable((By.ID, "election"))
        )
        Select(election).select_by_visible_text("AC - GENERAL")
        time.sleep(2)

        # fourth dropdown: states
        state = self.wait.until(
            EC.element_to_be_clickable((By.ID, "states"))
        )
        Select(state).select_by_visible_text("Maharashtra")

        # waiting for fifth dropdown: phase
        phase = self.wait.until(
            EC.element_to_be_clickable((By.ID, "phase"))
        )
        time.sleep(2)
        # this was surprising.
        # on the site that the field has -
        # value as 1 but its saved as value="3"
        Select(phase).select_by_visible_text("1")

        # sixth dropdown: constituency
        constituency = self.wait.until(
            EC.element_to_be_clickable((By.ID, "constId"))
        )
        time.sleep(2)
        Select(constituency).select_by_visible_text("BELAPUR")

        time.sleep(2)

        print("Now completed the first part i.e., applying filters.")

        filter_button = self.driver.find_element(By.NAME, "submitName")
        filter_button.click()

        time.sleep(5)

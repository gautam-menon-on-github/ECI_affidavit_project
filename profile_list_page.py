from selenium.webdriver.common.by import By

class ProfileListPage:

    def __init__(self, driver):
        self.driver = driver

    def collect_profile_urls(self):
        # there are 10 candidates on the page.
        # so we click "View more" for one candidate to view profile.
        # this creates list of profile urls.
        profiles = [
            a.get_attribute("href")
            for a in self.driver.find_elements(By.TAG_NAME, "a")
            if "View more" in a.text
        ]

        # just to check if i've got a valid List[String]
        print(profiles)

        return profiles

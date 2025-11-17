from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import json

from scraper_for_profiles import ScraperForProfiles

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://affidavit.eci.gov.in/')

wait = WebDriverWait(driver, 10)   # keeping it default at 10 seconds


# the first dropdown: election type
election_type = wait.until(
    EC.element_to_be_clickable((By.ID, "electionType"))
)
Select(election_type).select_by_value("27-AC-GENERAL-3-51")

# waiting for elements in the next dropdown to be loaded
time.sleep(2)


# second dropdown: election
election = wait.until(
    EC.element_to_be_clickable((By.ID, "election"))
)
Select(election).select_by_visible_text("AC - GENERAL")
time.sleep(2)

# fourth dropdown: states
state = wait.until(
    EC.element_to_be_clickable((By.ID, "states"))
)
Select(state).select_by_visible_text("Maharashtra")


# waiting for fifth dropdown: phase
phase = wait.until(
    EC.element_to_be_clickable((By.ID, "phase"))
)
time.sleep(2)
# this was surprising. 
# on the site that the field has -
# value as 1 but its saved as value="3"
Select(phase).select_by_visible_text("1")


# sixth dropdown: constituency
constituency = wait.until(
    EC.element_to_be_clickable((By.ID, "constId"))
)
time.sleep(2)
Select(constituency).select_by_visible_text("BELAPUR")

time.sleep(2)

print("Now completed the first part i.e., applying filters.")

filter_button = driver.find_element(By.NAME, "submitName")
filter_button.click()

time.sleep(5)

################################################################################3
# now onto Step 2: downloading the candidate affidavit pdfs
################################################################################

# there are 10 candidates on the page.
# so we click "View more" for one candidate to view profile.
# this creates list of profile urls.
profiles = [
    a.get_attribute("href")
    for a in driver.find_elements(By.TAG_NAME, "a")
    if "View more" in a.text
]

# just to check if i've got a valid List[String]
print(profiles)

time.sleep(8)
driver.quit()

# creating a list of dictionaries as per the sample given output format.
# I've saved the fields we don't have data for as None.
candidates = []

# there are only 10 profiles on a page hence range(10)
for i in range(10):
    profile_scraper = ScraperForProfiles()
    candidate_name, address = profile_scraper.scrape_profile(profiles[i])
    candidates.append({
        "candidate_name" : candidate_name,
        "pan" : None,
        "address" : address,
        "total_assets" : None
    })

print("\n")
print(candidates)

# writing the candidates list into json file
file_path = 'candidate_data.json'
with open(file_path, 'w') as f:
    json.dump(candidates, f, indent=4)

print("\n\nDone!")
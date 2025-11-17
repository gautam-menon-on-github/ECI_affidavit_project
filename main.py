import time
import json

from base_scraper import BaseScraper
from filter_page import FilterPage
from profile_list_page import ProfileListPage
from profile_scraper import ProfileScraper


def scrape_all_profiles(driver, profiles):
    # creating a list of dictionaries as per the sample given output format.
    # I've saved the fields we don't have data for as None.
    candidates = []

    # there are only 10 profiles on a page hence range(10)
    profile_scraper = ProfileScraper(driver)

    for i in range(10):
        candidate_name, address = profile_scraper.scrape_profile(profiles[i])
        candidates.append({
            "candidate_name": candidate_name,
            "pan": None,
            "address": address,
            "total_assets": None
        })

    print("\n")
    print(candidates)

    return candidates


def save_to_json(candidates):
    # writing the candidates list into json file
    file_path = 'candidate_data.json'
    with open(file_path, 'w') as f:
        json.dump(candidates, f, indent=4)

    print("\n\nDone!")


def main():
    base = BaseScraper()
    driver = base.driver
    wait = base.wait

    # Step 1: Apply filters
    filter_page = FilterPage(driver, wait)
    filter_page.apply_filters()

    # Step 2: Collect candidate profile URLs
    profile_list_page = ProfileListPage(driver)
    profiles = profile_list_page.collect_profile_urls()

    time.sleep(3)

    # Step 3: Scrape profiles
    candidates = scrape_all_profiles(driver, profiles)

    # Step 4: Save results
    save_to_json(candidates)

    base.quit()


if __name__ == "__main__":
    main()

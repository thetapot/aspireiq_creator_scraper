# main.py
from browser_manager import open_and_wait_for_user_close, open_chrome_with_profile
from filters import select_reach_and_engagement_filter
from scraper import scrape_all_pages  # Import the function to scrape all pages
import time


def main():
    # Step 1: Open the browser and wait for the user to close it (login step)
    open_and_wait_for_user_close()

    # Define a single pair of min and max followers (6000 and 20,000)
    min_follower = 6000
    max_follower = 8000

    # Define a single pair of min and max likes (500 and 50,000)
    min_like = 500
    max_like = 50000

    # Age selection as boolean (True to select, False to skip)
    age_options = {
        "13-17": True,
        "18-24": True,
        "25-34": True,
        "35-44": True,
        "45-64": True,
        "65+": True
    }

    # Gender selection ("All", "Male", or "Female")
    gender_choice = "male"  # Example: You can change this to "all" or "female"

    # Multiple locations and languages
    locations = ["United States", "United Kingdom"]  # You can specify more locations
    languages = ["English", "Spanish"]  # You can specify more languages

    # Step 2: Re-open the browser and load the page
    driver = open_chrome_with_profile()
    driver.get(
        "https://community.aspireiq.com/client/Fo9cITmb9lG60RzwcppmtMEG7RCCYcKI/app/KyXOg4RiEupXxAFkWh3qnud6nX3tIWb4")

    # Pause for 5 seconds so you can visually confirm the page is loaded
    print("Pausing for 5 seconds to confirm the page is loaded.")
    time.sleep(5)

    # Step 3: Apply the follower, likes, age filters, gender selection, locations, and languages
    print(
        f"Applying filters: Followers between {min_follower} and {max_follower}, likes between {min_like} and {max_like}, age groups, gender ({gender_choice.title()}), locations ({locations}), and languages ({languages}).")
    select_reach_and_engagement_filter(driver, min_follower, max_follower, min_like, max_like, age_options,
                                       gender_choice, locations, languages)

    # Pause for 5 seconds after applying the filters so you can visually confirm the action
    print("Pausing for 5 seconds after applying the filter.")
    time.sleep(5)

    # Step 4: Scrape all the pages and save to a CSV with dynamic filename
    print("Starting to scrape creators across all pages...")
    scrape_all_pages(driver, min_follower=min_follower, max_follower=max_follower, max_pages=500)

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    main()
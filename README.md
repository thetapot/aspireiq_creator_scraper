Aspire Scraper

This project is a web scraper for AspireIQ (https://community.aspireiq.com) that extracts creator details such as usernames and profile links from the AspireIQ platform. The scraper allows you to filter creators based on criteria like follower count, likes per post, demographics, locations, and languages. It can scrape up to 500 pages of creator data, save it to a CSV file, and dynamically name the file with the scrape date and follower range.

Features
- Automated Login: Uses Chrome profile to bypass the need for manual login each time.
- Custom Filters: Allows you to specify criteria such as follower count, likes, gender, age, location, and languages.
- Scraping Multiple Pages: The scraper can navigate up to 500 pages and gather creator data from each.
- CSV Export: Data is saved in a dynamically named CSV file, including the follower range and scrape date.
- Error Handling: Gracefully handles errors during scraping and navigation.

File Structure
```
aspire_scrape/
│
├── main.py                 # Entry point of the program
├── browser_manager.py       # Manages browser setup and profile
├── filters.py               # Handles filter setup (followers, likes, demographics, etc.)
├── scraper.py               # Handles scraping of creator details from multiple pages
└── README.txt               # This file, detailing project setup and usage
```
Setup Instructions

Prerequisites
- Python 3.8+: This project uses Python, so you will need to have Python installed on your machine.
- Google Chrome: The scraper uses Selenium with Chrome WebDriver to automate the browsing.
- ChromeDriver: ChromeDriver is a separate executable that Selenium uses to control Chrome. The webdriver-manager package automatically installs and manages the correct version for you.

Required Python Packages

To run this project, you'll need the following Python packages:
- selenium: WebDriver for browser automation.
- webdriver-manager: Automatically manages the installation of the correct ChromeDriver version.

You can install these packages using pip:
pip install selenium webdriver-manager

Setting up Chrome Profile for Automated Login
1. Set up a Chrome Profile:
    - Go to Chrome settings and create a new profile (if you don't want to use your default profile).
    - Log into the AspireIQ platform using your credentials and save the login in the browser.

2. Profile Path:
    - Note down the path of the Chrome profile (it might look like "/Users/yourname/Library/Application Support/Google/Chrome/Profile 1" on macOS or "C:/Users/yourname/AppData/Local/Google/Chrome/User Data/Profile 1" on Windows).
    - The path will be automatically detected based on your OS, so no manual input of the path is necessary.

How to Run

1. Clone the Repository:
git clone https://github.com/thetapot/aspireiq_creator_scraper.git cd aspire_scrape

2. Run the Scraper:
Run the main.py script to start the scraper:
python3 main.py


Program Flow
1. Login Handling: The browser opens using the saved profile, so you don't need to log in manually each time. You can close the browser window once logged in.
2. Filter Setup: The script applies filters such as follower count, likes, demographics, location, and language.
3. Scraping: The scraper then navigates through the pages, gathering creator details.
4. CSV Export: The scraped data is saved in a CSV file named according to the follower range and scrape date. For example: creators_6000_to_20000_2024_09_15.csv.

Example CSV Output

The CSV file will include two columns:

| username           | link                                 |
|--------------------|--------------------------------------|
| theshaemarie        | http://www.instagram.com/theshaemarie |
| john_doe           | http://www.instagram.com/john_doe    |

Customizing Filters

In main.py, you can adjust the following filters:
- Follower Count: Modify min_follower and max_follower variables.
- Likes per Post: Modify min_like and max_like variables.
- Age Groups: Adjust the age_options dictionary to choose which age groups to select.
- Gender: Change the gender_choice variable to "male", "female", or "all".
- Locations & Languages: Add more locations or languages to the locations and languages lists.

Project Details
- Language: Python 3.x
- Browser: Google Chrome
- Libraries:
  - Selenium: For browser automation.
  - webdriver-manager: For managing ChromeDriver installations.

Troubleshooting

- Browser Not Opening: Ensure the profile_path is correctly set in browser_manager.py.
- Login Not Persisting: Ensure you are logged into the Chrome profile used for the browser automation.
- Selenium Errors: Ensure Chrome is up to date, and the correct version of ChromeDriver is installed via webdriver-manager.

Future Improvements

- Pagination Control: Add more flexible controls for handling different pagination mechanisms.
- Scraping More Data: Expand the scraper to gather more information such as engagement rates, location, or other metrics.
- Multithreading: For faster scraping, implement multithreading to parallelize page scraping.

License

This project is licensed under the MIT License - see the LICENSE file for details.



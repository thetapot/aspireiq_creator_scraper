# filters.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


def input_keyword(driver, keyword):
    """
    This function inputs a keyword in the first text input field.
    It deletes any existing content by pressing backspace and then inputs the keyword.
    """
    try:
        # Locate the first text input (search bar) and clear its content
        keyword_input = driver.find_elements(By.CLASS_NAME, "_input_c76r6_251")[0]  # First occurrence
        keyword_input.click()
        keyword_input.send_keys(Keys.CONTROL + "a")  # Select all text (Command + A for macOS)
        keyword_input.send_keys(Keys.BACKSPACE)  # Delete current text
        time.sleep(1)  # Short pause

        # Input the new keyword
        keyword_input.send_keys(keyword)
        keyword_input.send_keys(Keys.ENTER)
        print(f"Keyword '{keyword}' set.")
        time.sleep(1)  # Short pause to let the changes apply

    except Exception as e:
        print(f"Error setting keyword: {e}")


def select_gender(driver, gender_choice):
    """
    This function selects the gender radio button based on the user's input: "All", "Male", or "Female".
    """
    gender_choice = gender_choice.title()  # Normalize capitalization

    # Dictionary mapping gender choices to XPath or class-based selections
    gender_radio_buttons = {
        "All": "//div[@class='_dot_1ef8j_46'][following-sibling::div[contains(text(), 'All')]]",
        "Male": "//div[@class='_dot_1ef8j_46'][following-sibling::div[contains(text(), 'Male')]]",
        "Female": "//div[@class='_dot_1ef8j_46'][following-sibling::div[contains(text(), 'Female')]]"
    }

    # Step 1: Select the appropriate radio button for the gender choice
    try:
        gender_button = driver.find_element(By.XPATH, gender_radio_buttons[gender_choice])
        gender_button.click()
        print(f"Selected gender: {gender_choice}")
    except Exception as e:
        print(f"Error selecting gender {gender_choice}: {e}")


def select_creator_demographics(driver, age_options, gender_choice):
    """
    This function clicks the 'Creator Demographics' section and selects the age checkboxes and gender radio button
    based on the user's input (age_options and gender_choice).
    """
    # Step 1: Click the 'Creator Demographics' section to expand it
    try:
        demographics_button = driver.find_element(By.XPATH, "//span[contains(text(),'Creator Demographics')]")
        demographics_button.click()
        time.sleep(2)  # Allow the section to expand
    except Exception as e:
        print(f"Error clicking 'Creator Demographics': {e}")
        return

    # Step 2: Check the age checkboxes based on the user's input
    checkboxes = driver.find_elements(By.CLASS_NAME, "_Checkbox_1v8tf_169")

    # Age groups we are checking
    age_groups = ["13-17", "18-24", "25-34", "35-44", "45-64", "65+"]

    # Shift the checkbox index by 2 to match the correct occurrence
    for i, age in enumerate(age_groups):
        try:
            if age_options[age]:
                checkbox = checkboxes[i + 2].find_element(By.CLASS_NAME, "_box_1v8tf_169")  # Shifted by 2
                checkbox.click()
                print(f"Checked age group: {age}")
            else:
                print(f"Skipped age group: {age}")
        except Exception as e:
            print(f"Error checking age group {age}: {e}")

    # Step 3: Select the gender radio button
    select_gender(driver, gender_choice)


def input_location_and_language(driver, locations, languages):
    """
    This function inputs multiple locations and languages into the respective fields
    based on the user's input, after gender selection but before applying filters.
    After typing each value, it will pause for one second and select the first suggestion.
    """
    try:
        # Step 1: Input each location
        location_input = driver.find_elements(By.CLASS_NAME, "_input_vi7i2_245")[0]  # 1st occurrence
        for location in locations:
            location_input.click()
            location_input.clear()  # Clear any existing value
            location_input.send_keys(location)
            time.sleep(3)  # Pause for the suggestions to load

            # Select the first suggestion from the dropdown
            first_suggestion = driver.find_element(By.CLASS_NAME, "_option_vi7i2_320")
            first_suggestion.click()
            print(f"Location set to: {location}")
            time.sleep(3)  # Small pause between entries
    except Exception as e:
        print(f"Error setting location: {e}")

    try:
        # Step 2: Input each language
        language_input = driver.find_elements(By.CLASS_NAME, "_input_vi7i2_245")[1]  # 2nd occurrence
        for language in languages:
            language_input.click()
            language_input.clear()  # Clear any existing value
            language_input.send_keys(language)
            time.sleep(1)  # Pause for the suggestions to load

            # Select the first suggestion from the dropdown
            first_suggestion = driver.find_element(By.CLASS_NAME, "_option_vi7i2_320")
            first_suggestion.click()
            print(f"Language set to: {language}")
            time.sleep(1)  # Small pause between entries
    except Exception as e:
        print(f"Error setting language: {e}")


def select_reach_and_engagement_filter(driver, keyword, min_follower, max_follower, min_like, max_like, age_options,
                                       gender_choice, locations, languages):
    """
    This function clicks the 'Reach & Engagement' and 'Creator Demographics' sections,
    inputs the keyword, min_follower, max_follower, min_like, max_like values, and applies the filter.
    It also selects the age checkboxes and gender radio button under 'Creator Demographics',
    and then manually types in multiple locations and languages, selecting the first suggestion for each.
    """
    # Step 1: Input the keyword in the first text input field
    input_keyword(driver, keyword)

    # Step 2: Open the 'Reach & Engagement' filter section
    try:
        reach_engagement_button = driver.find_element(By.XPATH, "//span[contains(text(),'Reach & Engagement')]")
        reach_engagement_button.click()
        time.sleep(2)  # Allow time for the section to expand
    except Exception as e:
        print(f"Error clicking 'Reach & Engagement' filter: {e}")
        return

    # Step 3: Set the Min Followers
    try:
        min_follower_input = driver.find_elements(By.CLASS_NAME, "_input_c76r6_251")[1]
        actions = ActionChains(driver)
        actions.double_click(min_follower_input).perform()
        min_follower_input.send_keys(Keys.BACKSPACE * len(min_follower_input.get_attribute('value')))
        min_follower_input.send_keys(str(min_follower))
        min_follower_input.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error setting min follower count: {e}")
        return

    # Step 4: Set the Max Followers
    try:
        max_follower_input = driver.find_elements(By.CLASS_NAME, "_input_c76r6_251")[2]
        actions.double_click(max_follower_input).perform()
        max_follower_input.send_keys(Keys.BACKSPACE * len(max_follower_input.get_attribute('value')))
        max_follower_input.send_keys(str(max_follower))
        max_follower_input.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error setting max follower count: {e}")
        return

    # Step 5: Set the Min Likes
    try:
        min_like_input = driver.find_elements(By.CLASS_NAME, "_input_c76r6_251")[3]
        actions.double_click(min_like_input).perform()
        min_like_input.send_keys(Keys.BACKSPACE * len(min_like_input.get_attribute('value')))
        min_like_input.send_keys(str(min_like))
        min_like_input.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error setting min likes count: {e}")
        return

    # Step 6: Set the Max Likes
    try:
        max_like_input = driver.find_elements(By.CLASS_NAME, "_input_c76r6_251")[4]
        actions.double_click(max_like_input).perform()
        max_like_input.send_keys(Keys.BACKSPACE * len(max_like_input.get_attribute('value')))
        max_like_input.send_keys(str(max_like))
        max_like_input.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print(f"Error setting max likes count: {e}")
        return

    # Step 7: Select Creator Demographics (Age Groups and Gender)
    select_creator_demographics(driver, age_options, gender_choice)

    # Step 8: Input multiple locations and languages, selecting the first suggestion for each
    input_location_and_language(driver, locations, languages)

    # Step 9: Click the "Apply Search & Filters" button
    try:
        apply_button = driver.find_element(By.XPATH, "//div[contains(text(),'Apply Search & Filters')]")
        apply_button.click()
        time.sleep(2)  # Wait for the filters to be applied
        print(
            f"Filters applied for followers between {min_follower} and {max_follower}, likes between {min_like} and {max_like}, and demographics set.")
    except Exception as e:
        print(f"Error applying filters: {e}")
        return
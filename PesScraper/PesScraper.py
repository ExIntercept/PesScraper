##########################################DONT FORGET TO pip install selenium in Command Prompt###########################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import logging
import time
import os



# Function to initialize the browser in headless mode
def initialize_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Enable headless mode
    options.binary_location = r"chrome.exe"
    browser = webdriver.Chrome(options=options)
    return browser

# Function to create or append to output.csv
def setup_csv():
    header = ["PRN", "SRN", "NAME", "CLASS", "SECTION", "Cycle", "Department", "Branch", "Institute"]
    if not os.path.isfile('output.csv'):
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)

def idBuilder(campus, date, branch):
    if campus.upper() == "RR":
        iD = f"PES1UG{date}{branch.upper()}"
    elif campus.upper() == "EC":
        iD = f"PES2UG{date}{branch.upper()}"
    return iD

# Function to scrape data from the website
def scrape_data(browser, input_value):
    
    button_clicked = False
    browser.get("https://www.pesuacademy.com/Academy/")

    # Wait for the button to be present
    try:
        if not button_clicked:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "knowClsSection")))
            button = browser.find_element(By.ID, "knowClsSection")
            button.click()
            button_clicked = True  # Update the flag to indicate that the button has been clicked


        # Locate the Enter Text field and input the value
        input_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='knowClsSectionModalLoginId']")))
        input_field.clear()

        # Use ActionChains to simulate typing as the input might require that
        ActionChains(browser).send_keys(input_value).perform()

        # Wait for the search button to be clickable
        search_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "knowClsSectionModalSearch")))
        search_button.click()

        # Wait for all result elements to be present
        result_elements = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="knowClsSectionModalTableDate"]/tr/td')))

        # Extract all results and save them to the output CSV
        results = [element.text for element in result_elements]

        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([input_value] + results)

        logging.info(f"Scraped data for input: {input_value}")

    except TimeoutException:
        logging.warning(f"Timeout waiting for element 'knowClsSection' for input: {input_value}")
    except Exception as e:
        logging.error(f"Error during scraping for input {input_value}: {e}")

    # Sleep to avoid detection or rate limiting
    time.sleep(2)

# Main function to read input CSV and perform scraping
def main():
    campus = input("Enter the campus(RR or EC): ")
    date = input("Enter join year(e.g., 23): ")
    branch = input("Enter the branch (e.g., CS): ")
    start = int(input("Enter the start number: "))
    stop = int(input("Enter the stop number: "))
    iD = idBuilder(campus, date, branch)
    print(iD)
    browser = initialize_browser()
    setup_csv()

    scrapeNum = 0

    for number in range(start, stop + 1):
        input_value = f"{iD}{number:03d}"
        scrape_data(browser, input_value)
        scrapeNum += 1
        print(f"Number of iDs scraped: {scrapeNum}")

    # Close the browser after processing all inputs
    browser.quit()

if __name__ == "__main__":
    main()
    input("Press enter to exit")

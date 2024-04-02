#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
companies = ['https://www.goodandgold.com/careers#job-listings', 
            'https://sproutbox.co/careers/', 
            'https://apply.workable.com/intuitive-digital/#jobs',
            'https://www.fish-marketing.com/contact-us/careers/',
            'https://www.strategicmarketinginc.com/about/#company',
            'https://www.portlandseogrowth.com/careers/',
            'https://charltonmarketing.com/careers/',
            'https://swift.co/careers',
            'https://deksia.com/employment',
            'https://www.gradybritton.com/careers',
            'https://murmurcreative.com/careers/',
            'https://elevatedthird.applytojob.com/apply/',
            ]
phrases = ['No available positions', "No positions", "Sorry", "No job", "No current", "No open", 'None available', 'Don\'t have', 'don\'t currently', 'No openings']
tabs = []

def getText(driver, website):
    driver.get(website) # Webpage to scrape
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll to bottom to lazy load everything
    time.sleep(1) # Wait to ensure lazy load
    webpage_text = driver.find_element(By.CSS_SELECTOR, 'body').text.upper() # Assigning all text to variable, setting to uppercase
    return webpage_text


def main(companies):
    for company in companies:
        try:
            text = getText(driver, company)
            if text is None:
                print("Error retrieving text for ", company)
            elif any(phrase.upper() in text for phrase in phrases):
                print(color.RED, "No positions available for", company, color.END)
            else:
                print(color.GREEN, "There are jobs available for", company, color.END)
                tabs.append(company)
        except Exception as e:
            print("Error:", e)
    
    driver.close()  # Close the original browser window
    
    driver2 = webdriver.Chrome() # New webdriver instance b/c closed other one
    for job_company in tabs:
        driver2.execute_script("window.open('" + job_company + "', '_blank')")

    print('---------------------------------')
    input("Press any key to close the browser...") 
    driver.quit()

main(companies)

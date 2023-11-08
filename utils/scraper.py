from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium import webdriver

# Function to scrape data and save to an Excel file
def scrape_to_excel(driver, table_selector, excel_filename):
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, table_selector))
    )
    table = driver.find_element(By.CSS_SELECTOR, table_selector)


    headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]


    data = [
        [cell.text for cell in row.find_elements(By.TAG_NAME, "td")]
        for row in table.find_elements(By.TAG_NAME, "tr")
        if row.find_elements(By.TAG_NAME, "td")  # Exclude rows without data cells
    ]
    df = pd.DataFrame(data, columns=headers)
    df.to_excel(excel_filename, index=False)
    print(f'Data saved to {excel_filename}')

# Function to click on the navigation tab
def click_nav_tab(driver, nav_tab_selector):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, nav_tab_selector))
    ).click()

# function to scrape data
def scrape_data(driver, url):
    try:
        # Open the website
        driver.get(url)
        
        # Scrape daily data
        scrape_to_excel(driver, "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section.js-table-wrapper.common-table-comp.scroll-view > div.common-table-wrapper > div > table", 'data/daily.xlsx')
        
        # Click the weekly tab and scrape weekly data
        click_nav_tab(driver, "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section.js-table-wrapper.common-table-comp.scroll-view > section.table-nav.common-section > div.start-side > nav > ul > li:nth-child(2)")
        scrape_to_excel(driver, "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section.js-table-wrapper.common-table-comp.scroll-view > div.common-table-wrapper > div > table", 'data/weekly.xlsx')
        
        # Click the monthly tab and scrape monthly data
        click_nav_tab(driver, "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section.js-table-wrapper.common-table-comp.scroll-view > section.table-nav.common-section > div.start-side > nav > ul > li:nth-child(3)")
        scrape_to_excel(driver, "#js-main-container > section.main-container.container > div > section.instrument.js-section-content > section.js-table-wrapper.common-table-comp.scroll-view > div.common-table-wrapper > div > table", 'data/monthly.xlsx')

    finally:
        # Close the driver
        driver.quit()

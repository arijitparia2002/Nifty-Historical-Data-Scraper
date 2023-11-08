from selenium import webdriver
from utils.scraper import scrape_data
from datetime import datetime, timedelta
import time

def main():
    # Initialize the web driver
    driver_path = 'drivers/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)

    # Get the current date
    current_date = datetime.now()

    # Calculate the date one year ago from the current date
    one_year_ago = current_date - timedelta(days=365)

    # Convert the dates to Unix timestamps
    end_date_timestamp = int(time.mktime(current_date.timetuple()))
    start_date_timestamp = int(time.mktime(one_year_ago.timetuple()))
    
    # URL to be scraped
    # url = 'https://in.investing.com/indices/s-p-cnx-nifty-historical-data'
    url = f"https://in.investing.com/indices/s-p-cnx-nifty-historical-data?end_date={end_date_timestamp}&st_date={start_date_timestamp}"
    
    # Perform the scraping
    scrape_data(driver, url)

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()

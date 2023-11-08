from selenium import webdriver
from utils.scraper import scrape_data

def main():
    # Initialize the web driver
    driver_path = 'drivers/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    
    # URL to be scraped
    url = 'https://in.investing.com/indices/s-p-cnx-nifty-historical-data'
    
    # Perform the scraping
    scrape_data(driver, url)

    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()

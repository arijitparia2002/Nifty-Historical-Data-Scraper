# Selenium Automation for Nifty Historical Data

This project contains a Python script that uses Selenium to automate the process of scraping historical data for the S&P CNX Nifty index from the Investing.com website. It navigates to the historical data page, changes the date range to the last year, and scrapes the daily, weekly, and monthly data tables, saving them into Excel files.

## Prerequisites

Before running this project, make sure you have the following installed:
- Python 3.6+
- Selenium
- pandas
- ChromeDriver (Make sure it matches the version of your Chrome browser)
- Create a directory named `data` in the root directory

It's recommended to use a virtual environment.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/nifty-historical-data-scraper.git
cd nifty-historical-data-scraper
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the scraper, simply execute the `main.py` script:

```bash
python main.py
```

The script will generate three Excel files with the data:
- `data/daily.xlsx` for daily data
- `data/weekly.xlsx` for weekly data
- `data/monthly.xlsx` for monthly data

## Structure

- `main.py`: Main script to run the scraper.
- `data/`: Directory where scraped data will be saved as Excel files.
- `drivers/`: Directory containing the ChromeDriver executable.
- `requirements.txt`: File containing the list of packages to install.
- `.gitignore`: File specifying untracked files that Git should ignore.

## Contributing

Feel free to fork the project and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is for educational purposes only. Make sure you have permission to scrape the website and you comply with their terms of service.


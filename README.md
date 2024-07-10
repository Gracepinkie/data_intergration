ShopRite Grocery Data Scraper and SQLite Integration

Description
This project scrapes grocery product data from ShopRite's website and stores it in a SQLite database. It includes Python scripts for scraping data using BeautifulSoup, storing data in an SQLite database (shoprite.db), and saving scraped data into CSV and JSON formats.


Querying the database:

You can query the shoprite.db SQLite database using SQLite command line tools or integrate it with your Python code for further analysis or application.

Project Structure
CSV_file.py: Python script to scrape ShopRite grocery data and store it in SQLite.
shoprite.db: SQLite database file where scraped data is stored.
shoprite.csv: CSV file containing scraped grocery data.
shoprite.json: JSON file containing scraped grocery data.
Dependencies
requests: For making HTTP requests to fetch web pages.
beautifulsoup4: For parsing HTML content.
pandas: For data manipulation and exporting data to CSV and JSON formats.


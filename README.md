# Web Scraper

## Description

This project is a web scraper that extracts data from specified web pages and saves it to MongoDB.

## Setup

### Prerequisites

- Python 3.8+
- MongoDB
- PostgreSQL

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Its-Shreya/webscraper.git
    cd webscraper
    ```

2. Install dependencies:
    bash
    pip install requests beautifulsoup4 pymongo


3. Configure database settings in the script.

### Usage

Run the scraper:
```bash
python scraper.py

Explanation of the Code:

Library Imports:
requests: To send HTTP requests.
BeautifulSoup from bs4: To parse HTML and XML documents.
logging: To log error messages.
pymongo: To interact with MongoDB.

Logging Configuration:
logging.basicConfig: Configures logging to capture errors and save them to a file named scraper.log.

Database Connection String:
MONGO_URI: Connection string for MongoDB.

Function Definitions:

get_soup(url): Fetches the content of a URL and returns a BeautifulSoup object for parsing. Handles network errors and logs them.
save_to_mongo(data): Saves the given data to a MongoDB collection. Handles database connection errors and logs them.
scrape_dynamic_content(url): Scrapes dynamic content from the given URL, extracts the required data, and saves it to MongoDB.
scrape(): Main function that iterates through a list of URLs and calls scrape_dynamic_content for each.

Main Execution Block:

if __name__ == "__main__": scrape(): Executes the scrape function when the script is run directly.

Dependencies
requests
beautifulsoup4
pymongo

Error Handling
Errors encountered during scraping are logged to scraper.log

### Conclusion

This approach covers scraping dynamic content, persisting data to MongoDB and handling errors robustly.

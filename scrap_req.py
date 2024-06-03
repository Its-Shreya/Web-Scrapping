import requests  # Library for making HTTP requests
from bs4 import BeautifulSoup  # Library for parsing HTML and XML documents
import logging  # Library for logging errors and other information
from pymongo import MongoClient  # Library for interacting with MongoDB
import json  # Library for working with JSON data

# Configure logging to capture errors and save them to 'scraper.log'
logging.basicConfig(filename='scraper.log', level=logging.ERROR)

# Database connection string for MongoDB
MONGO_URI = "mongodb://localhost:27017/"

def get_soup(url):
    """
    Fetches the content of the URL and returns a BeautifulSoup object for parsing.

    Args:
    url (str): The URL to fetch the content from.

    Returns:
    BeautifulSoup object or None if an error occurs.
    """
    try:
        response = requests.get(url)  # Send a GET request to the URL
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return BeautifulSoup(response.text, 'html.parser')  # Parse the content with BeautifulSoup
    except requests.exceptions.RequestException as e:  # Handle any exceptions that occur
        logging.error(f"Error fetching {url}: {e}")  # Log the error message
        return None  # Return None if an error occurs

def save_to_mongo(data):
    """
    Saves the scraped data to a MongoDB collection.

    Args:
    data (dict): The data to be saved.
    """
    try:
        client = MongoClient(MONGO_URI)  # Connect to MongoDB
        db = client['scrapedb']  # Select the database
        collection = db['scraped_data']  # Select the collection
        collection.insert_one(data)  # Insert the data into the collection
    except Exception as e:  # Handle any exceptions that occur
        logging.error(f"Error saving to MongoDB: {e}")  # Log the error message

def scrape_static_content(url):
    """
    Scrapes static content from the provided URL and saves it to the MongoDB.

    Args:
    url (str): The URL to scrape the content from.
    """
    soup = get_soup(url)  # Get the parsed HTML content
    if not soup:  # If fetching or parsing failed, exit the function
        return

    # Extract static data. This example needs to be adjusted based on actual content structure
    data = {
        "site": "scrapethissite",
        "data_type": "static",
        "data": []
    }

    # Example extraction logic (modify based on actual content)
    for item in soup.select('.item'):  # Select elements with class 'item'
        data['data'].append({
            "name": item.select_one('.name').text,  # Extract text from child element with class 'name'
            "value": item.select_one('.value').text  # Extract text from child element with class 'value'
        })

    save_to_mongo(data)  # Save the data to MongoDB

def scrape_dynamic_content(url):
    """
    Scrapes dynamic content from the provided URL and saves it to the MongoDB.

    Args:
    url (str): The URL to scrape the content from.
    """
    soup = get_soup(url)  # Get the parsed HTML content
    if not soup:  # If fetching or parsing failed, exit the function
        return

    # Extract dynamic data. This example needs to be adjusted based on actual content structure
    data = {
        "site": "scrapethissite",
        "data_type": "dynamic",
        "data": []
    }

    # Example extraction logic (modify based on actual content)
    # Here, you would typically need to make additional requests to fetch dynamic data.
    for script in soup.find_all('script'):
        if 'var teamData' in script.text:
            json_text = script.text.split('var teamData =')[1].split(';')[0].strip()
            dynamic_data = json.loads(json_text)
            data['data'].extend(dynamic_data)

    save_to_mongo(data)  # Save the data to MongoDB

def scrape():
    """
    Main scraping function that processes a list of URLs.
    """
    urls = [
        "https://www.scrapethissite.com/pages/ajax-javascript/#2015",
        "https://www.scrapethissite.com/pages/forms/",
        "https://www.scrapethissite.com/pages/advanced/"
    ]
    for url in urls:  # Iterate through the list of URLs
        scrape_static_content(url)  # Scrape static content from each URL
        scrape_dynamic_content(url)  # Scrape dynamic content from each URL

if __name__ == "__main__":
    scrape()  # Execute the scraping function

import os
import time
import datetime
from requests_html import HTMLSession
from mysql.connector import Error
from db_connection import create_db_connection
from news_insert_modified import (execute_query,
                                  insert_reporter,
                                  insert_category,
                                  insert_news,
                                  insert_publisher,
                                  insert_image)

# Set the environment for Pyppeteer Chromium revision
PYPPETEER_CHROMIUM_REVISION = '1263111'
os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

def process_and_insert_news_data(connection, publisher_website, publisher, title, reporter, news_datetime, category, news_body, images, url):
    """
    Processes and inserts the scraped news data into the database.
    """
    try:
        # Insert category
        insert_category(connection, category, f"{category} description")
        category_id = get_category_id(connection, category)  # Retrieve the inserted category ID

        # Insert reporter
        insert_reporter(connection, reporter, f"{reporter}@{publisher_website}")
        reporter_id = get_reporter_id(connection, reporter)  # Retrieve the inserted reporter ID

        # Insert publisher
        insert_publisher(connection, publisher, f"{publisher}@{publisher_website}")
        publisher_id = get_publisher_id(connection, publisher)  # Retrieve the inserted publisher ID

        # Insert news article
        insert_news(connection, category_id, reporter_id, publisher_id, news_datetime, title, news_body, url)
        news_id = get_news_id(connection, title)  # Retrieve the inserted news ID

        # Insert images
        for image_url in images:
            insert_image(connection, news_id, image_url)

    except Error as e:
        print(f"Error while processing news data: {e}")

def single_news_scraper(url):
    """
    Scrapes a single news article from the provided URL.
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render(sleep=3)  # Ensure all elements are loaded

        # Extract details
        publisher_website = url.split('/')[2]
        publisher = publisher_website.split('.')[-2]

        title = response.html.find('h1', first=True).text
        reporter = response.html.find('.contributor-name', first=True).text
        news_datetime = response.html.find('time', first=True).attrs

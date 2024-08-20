import os
import time
import datetime
from requests_html import HTMLSession
from mysql.connector import Error
from db_connection import create_db_connection
from news_insert_modified import (execute_query, insert_reporter, get_reporter_id, insert_category,
                                  get_category_id, insert_news, get_news_id, insert_publisher, 
                                  get_publisher_id, insert_image)

# Set the environment variable for Pyppeteer Chromium revision
os.environ['PYPPETEER_CHROMIUM_REVISION'] = '1263111'

def process_and_insert_news_data(connection, publisher_website, publisher, title, reporter, news_datetime, category, news_body, images, url):
    """
    Process and insert news data into the database.
    """
    try:
        # Insert category and get its ID
        insert_category(connection, category, category) 
        category_id = get_category_id(connection, category)
        
        # Insert reporter and get its ID
        insert_reporter(connection, reporter, f"{reporter}@{publisher_website}")
        reporter_id = get_reporter_id(connection, reporter)
        
        # Insert publisher and get its ID
        insert_publisher(connection, publisher, publisher_website)
        publisher_id = get_publisher_id(connection, publisher)
        
        # Insert news article and get its ID
        insert_news(connection, category_id, reporter_id, publisher_id, news_datetime, title, news_body, url)
        news_id = get_news_id(connection, title)
        
        # Insert images associated with the news article
        for image_url in images:
            insert_image(connection, news_id, image_url)
    
    except Error as e:
        print(f"Error while processing news data: {e}")

def single_news_scraper(url):
    """
    Scrape a single news article from the provided URL.
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render()  # Render the page (downloads Chromium if necessary)
        
        # Extract publisher information
        publisher_website = url.split('/')[2]
        publisher = publisher_website.split('.')[-2]
        
        # Extract article details
        title = response.html.find('h1', first=True).text
        reporter = response.html.find('.contributor-name', first=True).text
        news_datetime = response.html.find('time', first=True).attrs['datetime']
        category = response.html.find('.print-entity-section-wrapper', first=True).text
        news_body = '\n'.join([p.text for p in response.html.find('p')])
        
        # Extract image URLs
        images = [img.attrs['src'] for img in response.html.find('img') if 'src' in img.attrs]
        
        return publisher_website, publisher, title, reporter, news_datetime, category, news_body, images

    except Exception as e:
        print(f"An error occurred while scraping the news: {e}")
        return None
    
    finally:
        session.close()

if __name__ == "__main__":
    # Establish database connection
    conn = create_db_connection()
    if conn:
        url = "https://www.prothomalo.com/business/economics/qergvfd5za"
        news_data = single_news_scraper(url)
        
        if news_data:
            publisher_website, publisher, title, reporter, news_datetime, category, news_body, images = news_data
            process_and_insert_news_data(conn, publisher_website, publisher, title, reporter, news_datetime, category, news_body, images, url)

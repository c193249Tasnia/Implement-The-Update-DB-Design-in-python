import os
import mysql.connector
from mysql.connector import Error
from db_connection import create_db_connection

def execute_query(connection, query, data=None):
    """Execute a SQL query with optional data and handle errors."""
    try:
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()

def insert_category(connection, name, description):
    """Insert a new category into the categories table."""
    query = "INSERT INTO categories (name, description) VALUES (%s, %s)"
    data = (name, description)
    execute_query(connection, query, data)

def get_category_id(connection, category_name):
    """Retrieve the category ID based on the category name."""
    query = "SELECT id FROM categories WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (category_name,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def insert_reporter(connection, name, email):
    """Insert a new reporter into the reporters table."""
    query = "INSERT INTO reporters (name, email) VALUES (%s, %s)"
    data = (name, email)
    execute_query(connection, query, data)

def get_reporter_id(connection, reporter_name):
    """Retrieve the reporter ID based on the reporter name."""
    query = "SELECT id FROM reporters WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (reporter_name,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def insert_publisher(connection, name, email):
    """Insert a new publisher into the publishers table."""
    query = "INSERT INTO publishers (name, email) VALUES (%s, %s)"
    data = (name, email)
    execute_query(connection, query, data)

def get_publisher_id(connection, publisher_name):
    """Retrieve the publisher ID based on the publisher name."""
    query = "SELECT id FROM publishers WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(query, (publisher_name,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def insert_news(connection, category_id, reporter_id, publisher_id, datetime, title, body, link):
    """Insert a new news article into the news table."""
    query = """
    INSERT INTO news (category_id, reporter_id, publisher_id, datetime, title, body, link)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (category_id, reporter_id, publisher_id, datetime, title, body, link)
    execute_query(connection, query, data)

def get_news_id(connection, title):
    """Retrieve the news ID based on the title."""
    query = "SELECT id FROM news WHERE title = %s"
    cursor = connection.cursor()
    cursor.execute(query, (title,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def insert_image(connection, news_id, image_url):
    """Insert a new image into the images table."""
    query = "INSERT INTO images (news_id, image_url) VALUES (%s, %s)"
    data = (news_id, image_url)
    execute_query(connection, query, data)

def insert_summary(connection, news_id, summary_text):
    """Insert a summary related to a news article."""
    query = "INSERT INTO summaries (news_id, summary_text) VALUES (%s, %s)"
    data = (news_id, summary_text)
    execute_query(connection, query, data)

# Example usage
if __name__ == "__main__":
    conn = create_db_connection()
    if conn:
        # Example inserts (Uncomment to use):
        # insert_category(conn, "Politics", "All news related to politics")
        # insert_reporter(conn, "John Doe", "john@example.com")
        # insert_publisher(conn, "News Corp", "contact@newscorp.com")
        
        # Example for inserting news:
        # category_id = get_category_id(conn, "Politics")
        # reporter_id = get_reporter_id(conn, "John Doe")
        # publisher_id = get_publisher_id(conn, "News Corp")
        # insert_news(conn, category_id, reporter_id, publisher_id, "2024-08-20 10:00:00", "Breaking News Title", "Detailed news body content...", "https://news.example.com/article")
        
        conn.close()

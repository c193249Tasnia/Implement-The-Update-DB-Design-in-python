import os
from requests_html import HTMLSession

# Set the Chromium revision for Pyppeteer
PYPPETEER_CHROMIUM_REVISION = '1263111'
os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION

def render_javascript(url):
    """
    Renders JavaScript on the specified URL and prints the page's HTML content.
    
    Parameters:
    url (str): The URL of the web page to render.
    
    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        response.html.render(retries=3, sleep=5, wait=10)  # Render JavaScript content
        print("Rendered web page content:\n", response.html.html[:500])  # Print first 500 characters for preview
    except Exception as e:
        print(f"An error occurred during JavaScript rendering: {e}")
    finally:
        session.close()

def extract_information(url):
    """
    Extracts the title and all links from the specified URL.
    
    Parameters:
    url (str): The URL of the web page to extract information from.
    
    Returns:
    None
    """
    session = HTMLSession()
    try:
        response = session.get(url)
        
        # Extract and print the title tag
        title_tag = response.html.find('h1', first=True)
        if title_tag:
            print("Title:", title_tag.text)
        else:
            print("No title tag found.")
        
        # Extract and print all links on the page
        links = response.html.find('a')
        print(f"{len(links)} links found:")
        for link in links:
            href = link.attrs.get('href', 'No href attribute')
            print(f"Link Text: {link.text}, Link href: {href}")
        
    except Exception as e:
        print(f"An error occurred during information extraction: {e}")
    finally:
        session.close()

def main():
    """
    Main function to execute web scraping examples.
    """
    url = 'https://example.com'
    
    print("Rendering JavaScript on the web page...")
    render_javascript(url)

    print("\nExtracting information from the web page...")
    extract_information(url)

if __name__ == "__main__":
    main()

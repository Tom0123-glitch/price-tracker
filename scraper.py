import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_price(url):
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        # Customize these selectors based on the website
        selectors = [
            ".price", 
            ".product-price",
            ".sale-price",
            "[itemprop='price']", 
            ".a-price-whole"  # Amazon Example
        ]

        for selector in selectors:
            price_element = soup.select_one(selector)
            if price_element:
                return price_element.text.strip()

    except Exception as e:
        print(f"Error fetching price for {url}: {e}")
    
    return None
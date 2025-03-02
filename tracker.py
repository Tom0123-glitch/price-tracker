import time
from db import get_products, update_price
from scraper import get_price
from notifier import send_email

def track_prices():
    products = get_products()

    for product in products:
        product_id, url, old_price = product
        new_price = get_price(url)

        if new_price and new_price != old_price:
            print(f"Price changed for {url}: {old_price} -> {new_price}")
            update_price(url, new_price)

            message = f"Price Update!\n{url}\nOld: {old_price}\nNew: {new_price}"
            send_email("Price Alert!", message)
            

if __name__ == "__main__":
    while True:
        track_prices()
        time.sleep(600)  # Check every 10 minutes



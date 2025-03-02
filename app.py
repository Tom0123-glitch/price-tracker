from flask import Flask, render_template, request, redirect
from db import add_product, get_products
from scraper import get_price

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        price = get_price(url)
        if price:
            add_product(url, price)

    products = get_products()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



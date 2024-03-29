import requests
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Define a URL for a news API
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

# Define API parameters
NEWS_API_KEY = "b969b3ff16c84732bf8b41ae5cdda4ab"
NEURFORGE_CATEGORY = "NeuroForge"

@app.route("/")
def index():
    # Fetch news from the API
    response = requests.get(
        NEWS_API_URL,
        params={
            "apiKey": b969b3ff16c84732bf8b41ae5cdda4ab, 
            "category": NEURFORGE_CATEGORY
        }
    )

    news = response.json().get("articles")

    return render_template("index.html", news=news)

@app.route("/article/<string:title>")
def article(title):
    # Fetch news from the API with the given title
    response = requests.get(
        NEWS_API_URL,
        params={
            "apiKey": b969b3ff16c84732bf8b41ae5cdda4ab, 
            "q": title,
            "pageSize": 1
        }
    )

    articles = response.json().get("articles")

    # Redirect to the first article's URL
    article_url = articles[0].get("url")

    return redirect(article_url)

if __name__ == "__main__":
    app.run()

import logging
from flask import Flask, render_template, request
from scraper import SimpleScraper
from analyzer import ToxicityAnalyzer
from post_cleaner import PostClean
from mongodb_handler import MongoDBHandler
from models import Post

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.route("/", methods=["GET", "POST"])
def index():
    posts = []

    if request.method == "POST":
        tag = request.form.get("tag")
        logging.info(f"📌 Hashtag received: {tag}")

        # 1. Scraping
        scraper = SimpleScraper(tag)
        try:
            raw_data: list[Post] = scraper.scrape_twitter_posts(10)
            if not raw_data:
                raise ValueError("No posts returned from scraper.")
            logging.info(f"✅ Scraped {len(raw_data)} posts.")
        except Exception as e:
            logging.error(f"❌ Error scraping Twitter posts: {e}")
            raw_data = scraper.simulate_twitter_posts(10)
            logging.info("ℹ️ Using simulated tweets instead.")

        for post in raw_data:
            logging.debug(f"Raw post: {post.content}")

        # 2. Cleaning
        cleaner = PostClean()
        cleaned_posts = cleaner.normalize_clean_tweets(raw_data)
        logging.info(f"🧹 Cleaned {len(cleaned_posts)} tweets.")
        for cp in cleaned_posts:
            logging.debug(f"Cleaned post: {cp.content}")

        # 3. Toxicity Analysis
        analyzer = ToxicityAnalyzer()
        analyzer.analyze(cleaned_posts)
        logging.info("🔍 Toxicity analysis completed.")
        for cp in cleaned_posts:
            logging.debug(f"Toxicity: {cp.toxicity} | Content: {cp.content[:40]}...")
        '''
        # 4. Store in MongoDB
        mongo = MongoDBHandler()
        mongo.insert_posts(cleaned_posts)
        logging.info("🗃️ Posts inserted into MongoDB.")
    '''
        posts = cleaned_posts

    return render_template("index.html", results=posts)


if __name__ == "__main__":
    logging.info("🌐 Flask app starting at http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000)

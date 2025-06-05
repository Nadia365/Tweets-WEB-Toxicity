from flask import Flask, render_template, request
from scraper import SimpleScraper
from analyzer import ToxicityAnalyzer
from dataset import SimpleDataset

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    posts = []
    if request.method == "POST":
        tag = request.form.get("tag")
        scraper = SimpleScraper(tag)
        analyzer = ToxicityAnalyzer()
        dataset = SimpleDataset()

        twitter_posts = scraper.scrape_twitter_posts(10)
        #fb_posts = scraper.simulate_facebook_posts(10)
       # all_posts = twitter_posts + fb_posts
        all_posts=twitter_posts
        analyzer.analyze(all_posts)
        dataset.save_to_csv(all_posts)

        posts = all_posts

    return render_template("index.html", results=posts)

if __name__ == "__main__":
    print("🌐 Flask app starting at http://localhost:5000 ...")
    app.run(host="0.0.0.0", port=5000)

import logging
import tweepy
from typing import List
from models import Post
import os
from dotenv import load_dotenv

load_dotenv('var.env')
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
class SimpleScraper:
    def __init__(self, tag: str):
        self.tag = tag
        self.twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN)

    def scrape_twitter_posts(self, limit: int = 10) -> List[Post]:
        logging.info(f"Scraping {limit} tweets with #{self.tag}")
        posts = []
        query = f"#{self.tag} lang:fr -is:retweet"
        try:
            response = self.twitter_client.search_recent_tweets(query=query, max_results=limit)
            if response.data:
                for tweet in response.data:
                    posts.append(Post(tweet.text, "Twitter"))
        except Exception as e:
            logging.error(f"Twitter scraping error: {e}")
        return posts

    def simulate_facebook_posts(self, limit: int = 10) -> List[Post]:
        return [Post(f"Fake Facebook post #{i} about #{self.tag}", "Facebook") for i in range(limit)]

import logging
import tweepy
from typing import List
from models import Post
import os
from dotenv import load_dotenv
import random

load_dotenv('var.env')
#BEARER_TOKEN = os.getenv("BEARER_TOKEN")
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAHup2AEAAAAAaDJ6uIMAz9m4%2FJIp1tuSqvPQtBA%3Dlx89suzJRbZMQG726y6g5yTkrXQ3Y8Iuj7I5cC0xjmc9dxNsUJ"
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
    def simulate_twitter_posts(self, limit: int = 10) -> List[Post]:
        positive_templates = [
            "Je me sens incroyablement bien aujourd'hui !",
            "La vie est belle, je suis reconnaissant pour chaque instant.",
            "Je vais mieux, merci pour tous vos messages de soutien ❤️",
            "Aujourd'hui est une bonne journée 😊",
            "Je suis plein d'espoir pour l'avenir #espoir",
            "Merci à mes amis pour leur soutien constant. #gratitude"
        ]

        negative_templates = [
            "Je me sens tellement seul et déprimé...",
            "Je n’ai aucune motivation pour sortir du lit.",
            "Tout me semble vide et sans sens.",
            "Encore une crise d'angoisse aujourd'hui.",
            "Personne ne comprend ce que je vis.",
            "Je suis fatigué de faire semblant que tout va bien."
        ]

        posts = []
        for _ in range(limit):
            sentiment = random.choice(["positive", "negative"])
            if sentiment == "positive":
                content = random.choice(positive_templates)
            else:
                content = random.choice(negative_templates)
            content += f" #{self.tag}"
            post = Post(content=content, platform="Twitter")
            post.classification = sentiment  # optional, for testing
            posts.append(post)

        return posts


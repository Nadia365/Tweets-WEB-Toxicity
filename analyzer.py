import logging
from detoxify import Detoxify
from typing import List
from models import Post

class ToxicityAnalyzer:
    def __init__(self):
        logging.info("Loading Detoxify model...")
        self.model = Detoxify("original")

    def analyze(self, posts: List[Post]) -> List[Post]:
        for post in posts:
            result = self.model.predict(post.content)
            post.toxicity = result["toxicity"]
            logging.info(f"Analyzed: '{post.content[:30]}...' => Toxicity: {post.toxicity:.4f}")
        return posts

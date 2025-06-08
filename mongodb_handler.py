# mongodb_handler.py

from pymongo import MongoClient
from typing import List
from models import Post

class MongoDBHandler:
    def __init__(self, uri="mongodb://localhost:27017", db_name="toxicity_db", collection_name="cleaned_posts"):
        self.client = MongoClient(uri)
        self.collection = self.client[db_name][collection_name]

    def insert_posts(self, posts: List[Post]) -> None:
        docs = [{"content": p.content, "platform": p.platform, "toxicity": p.toxicity} for p in posts]
        if docs:
            self.collection.insert_many(docs)

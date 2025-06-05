import csv
import logging
from typing import List
from models import Post

class SimpleDataset:
    def __init__(self, filename: str = "toxicity_dataset.csv"):
        self.filename = filename

    def save_to_csv(self, posts: List[Post]) -> None:
        logging.info(f"Saving results to {self.filename}")
        with open(self.filename, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Platform", "Content", "Toxicity"])
            for post in posts:
                writer.writerow([post.platform, post.content, f"{post.toxicity:.4f}"])
        logging.info("Dataset saved successfully.")

# post_cleaner.py

import logging
import re
from typing import List
from models import Post
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class PostClean:
    def __init__(self):
        self.stop_words = set(stopwords.words('french'))
        self.lemmatizer = WordNetLemmatizer()

    def remove_emoji(self, text: str) -> str:
        emoji_pattern = re.compile(
            "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE
        )
        return emoji_pattern.sub(r'', text)

    def normalize_tweet(self, tweet: str) -> str:
        tweet = self.remove_emoji(tweet)
        tweet = tweet.lower()
        tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet)
        tweet = re.sub(r'@\S+', '', tweet)
        tweet = re.sub(r'#\S+', '', tweet)
        tweet = re.sub(r'[^a-zA-Zàâçéèêëîïôûùüÿñæœ\s]', '', tweet)
        tweet = re.sub(r'^rt\s+', '', tweet)

        tokens = nltk.word_tokenize(tweet)
        tokens = [token for token in tokens if token not in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        return ' '.join(tokens)

    def normalize_clean_tweets(self, posts: List[Post]) -> List[Post]:
        logging.info('Nettoyage des tweets en cours...')
        clean_posts: List[Post] = []

        for post in posts:
            cleaned_text = self.normalize_tweet(post.content)
            clean_post = Post(content=cleaned_text, platform=post.platform)
            clean_posts.append(clean_post)
            logging.info(f"Cleaned: '{cleaned_text[:30]}...'")

        return clean_posts

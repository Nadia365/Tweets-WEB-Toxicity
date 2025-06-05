# Tweets-WEB-Toxicity
# 🧪 Toxicity Analyzer for Social Media Posts

This project is a Flask-based web application that scrapes Twitter posts based on a given hashtag, analyzes their toxicity using the [Detoxify](https://github.com/unitaryai/detoxify) model, and displays the results on a webpage. It is designed for French-language tweets and demonstrates the integration of web scraping, natural language processing, and frontend rendering.

---

## 🧩 Features

- 🔍 Scrapes recent tweets using a custom hashtag (via Twitter API v2).
- 🧠 Analyzes post toxicity using the Detoxify model.
- 📄 Displays post content, platform, and toxicity score.
- 💾 Saves analyzed posts to a CSV file for further processing.
- 🌐 Web-based interface built with Flask.

---

## 📂 Project Structure

├── app.py # Main Flask application
├── models.py # Data class for posts
├── scraper.py # Twitter scraping logic (via Tweepy)
├── analyzer.py # Detoxify-based sentiment analyzer
├── dataset.py # Utility for saving post data to CSV
├── templates/
│ └── index.html # Frontend template for user interaction
├── var.env # Environment file containing BEARER_TOKEN

## ⚙️ Requirements

- Python 3.8+
- [Flask](https://palletsprojects.com/p/flask/)
- [Tweepy](https://www.tweepy.org/)
- [Detoxify](https://github.com/unitaryai/detoxify)
- [dotenv](https://pypi.org/project/python-dotenv/)

##### Install dependencies:

```bash
pip install -r requirements.txt 

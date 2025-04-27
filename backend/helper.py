from typing import List
from playstore_scraper import fetch_search_suggestions
from models import ReviewSentiment, SentimentMetrics

def format_app_name(app_name: str):

    if not app_name.startswith("com."):
        app_name = fetch_search_suggestions(app_name, 1)[0]
    return app_name

def calculate_sentiment_metrics(sentiments: List[ReviewSentiment]) -> SentimentMetrics:

    if not sentiments:
        return SentimentMetrics(average_score=0, review_count=0)
    
    average_score = sum(item.sentiment_score for item in sentiments) / len(sentiments)
    return SentimentMetrics(
        average_score=average_score,
        review_count=len(sentiments)
    )
import asyncio
from typing import List
from transformers import pipeline
from models import ReviewSentiment, Review

sentiment_pipeline = pipeline(
    "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english"
)

_semaphore = asyncio.Semaphore(10)

def normalize_score(score: int, max_score: int = 5) -> float:
    return score / max_score

async def analyze_review(review: Review) -> ReviewSentiment:

    text = review.content
    score = review.score
    async with _semaphore:
        result = await asyncio.to_thread(sentiment_pipeline, text)
        label = result[0]["label"]
        sentiment_score = result[0]["score"]
        
        normalized_score = normalize_score(score)
        
        if label == "POSITIVE":
            final_score = (sentiment_score + normalized_score) / 2
        else:
            final_score = (1 - sentiment_score + normalized_score) / 2
        
        return ReviewSentiment(
            review_text=text,
            review_rating=score,
            label=label,
            sentiment_score=final_score,
        )


async def analyze_sentiments(texts: List[Review]) -> List[ReviewSentiment]:

    tasks = [analyze_review(text) for text in texts]
    return await asyncio.gather(*tasks)
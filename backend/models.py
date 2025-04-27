from pydantic import BaseModel, Field
from typing import List, Optional

class SentimentRequest(BaseModel):
    appName: str = Field(..., min_length=1, max_length=100, description="Google Play Store app name")
    reviewLimit: int = Field(100, ge=1, le=100, description="Number of reviews to fetch (default is 100)")

class ReviewSentiment(BaseModel):
    review_text: str = Field(..., description="Original review text")
    review_rating: int = Field(..., ge=1, le=5, description="Original review rating (1 to 5)")
    label: str = Field(..., description="Predicted sentiment label (e.g., 'POSITIVE' or 'NEGATIVE')")
    sentiment_score: float = Field(..., ge=0.0, le=1.0, description="Confidence score for the sentiment")

class SentimentResponse(BaseModel):
    average_score: float = Field(..., ge=0.0, le=1.0, description="Average sentiment score between 0 and 1")
    review_count: int = Field(..., ge=0, description="Number of reviews analyzed")
    details: Optional[List[ReviewSentiment]] = Field(None, description="Optional per-review sentiment details")
    app_name: str = Field(..., description="Formatted app name (e.g., 'com.whatsapp')")

class Review(BaseModel):
    content: str = Field(..., description="Review content")
    score: int = Field(..., ge=1, le=5, description="Review score (1 to 5)")

class SentimentMetrics(BaseModel):
    average_score: float
    review_count: int

class TypeaheadResponse(BaseModel):
    suggestions: List[str]
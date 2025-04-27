import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import SentimentRequest, SentimentResponse, TypeaheadResponse
from playstore_scraper import fetch_reviews, fetch_search_suggestions
from sentiment_analysis import analyze_sentiments
from helper import calculate_sentiment_metrics, format_app_name
from config import settings


app = FastAPI(
    title="Play Store Sentiment Analyzer",
    version="1.0.0",
    description="Fetches Google Play reviews and analyzes sentiment."
)

origins = [
    settings.CLIENT_HOST+":"+str(settings.CLIENT_PORT),
    "http://localhost"+":"+str(settings.CLIENT_PORT),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

@app.post("/sentiment", response_model=SentimentResponse, tags=["Sentiment"])
async def analyze_sentiment(request: SentimentRequest):
    
    app_details = format_app_name(request.appName)
    app_id = app_details['appId']
    formatted_app_name = app_details['title']
    try:
        reviews = await asyncio.to_thread(fetch_reviews, app_id, request.reviewLimit)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Error fetching reviews: {exc}")

    if not reviews:
        raise HTTPException(
            status_code=404,
            detail=f"No reviews found for app '{request.appName}'"
        )

    sentiments = await analyze_sentiments(reviews)
    sentiment_metrics = calculate_sentiment_metrics(sentiments)

    return SentimentResponse(
        average_score=sentiment_metrics.average_score,
        review_count=sentiment_metrics.review_count,
        details=sentiments,
        app_name=formatted_app_name,
    )

@app.get("/suggestions", response_model=TypeaheadResponse, tags=["Typeahead"])
async def typeahead(query: str):
    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required.")
    
    suggestions = fetch_search_suggestions(query, 5)
    suggestions = [s['title'] for s in suggestions if s['title'].lower().startswith(query.lower())]
    print(suggestions)
    return TypeaheadResponse(suggestions=suggestions)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.BACKEND_HOST,
        port=settings.BACKEND_PORT,
        reload=True
    )
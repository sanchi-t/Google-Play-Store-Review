from google_play_scraper import reviews, Sort, search
from typing import List
from models import Review, TypeaheadResponse


def fetch_reviews(app_name, limit) -> List[Review]:

    try:
        result, _ = reviews(
            app_name,
            lang='en',
            country='in',
            sort=Sort.NEWEST,
            count=limit,
        )
        reviews_list = [Review(content=r['content'], score=r['score']) for r in result]
        return reviews_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def fetch_search_suggestions(query: str, limit: int) -> TypeaheadResponse:

    try:
        result = search(
            query,
            lang="en", 
            country="in",
            n_hits=limit
        )
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
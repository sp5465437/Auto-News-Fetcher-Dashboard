import requests
from django.conf import settings
from .models import NewsArticle

def fetch_news_articles():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'in',
        'pageSize': 20,
        'apiKey': settings.NEWS_API_KEY  # Use from settings
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises exception for 4xx or 5xx

    data = response.json()
    articles = data.get('articles', [])

    count = 0
    for article in articles:
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')

        if title and not NewsArticle.objects.filter(title=title).exists():
            NewsArticle.objects.create(
                title=title,
                description=description or '',
                url=url or ''
            )
            count += 1

    return count

# news_app/utils.py

import requests
from django.conf import settings

def fetch_news_data():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',
        'pageSize': 20,
        'apiKey': settings.NEWS_API_KEY  # This will read from your settings.py
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # raises error if status_code != 200
    data = response.json()
    return data.get('articles', [])

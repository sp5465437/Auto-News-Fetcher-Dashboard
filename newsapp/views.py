from django.shortcuts import render, redirect
from .models import News
import requests
from django.utils.dateparse import parse_datetime

KEY = "189bfa84fda245e5a2af6b468a6b04ba"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={KEY}"

def fetch_news():
    r = requests.get(URL).json()
    for article in r.get('articles', []):
        title = article['title']
        if not News.objects.filter(title=title).exists():
            News.objects.create(
                title=title,
                summary = article.get("description") or "No summary available",
                source=article['source']['name'],
                published_at=parse_datetime(article['publishedAt'])
            )

def dashboard(request):
    articles = News.objects.all().order_by('-published_at')
    return render(request, 'index.html', {'articles': articles})

def fetch_news_view(request):
    fetch_news()
    return redirect('dashboard')

from django.shortcuts import render, redirect
from .models import NewsArticle
from .services import fetch_news_articles
from django.contrib import messages
from .utils import fetch_news_data  # Assuming you wrote a fetcher function here


def dashboard(request):
    articles = NewsArticle.objects.all().order_by('-published_at')
    sources = NewsArticle.objects.values_list('source', flat=True).distinct()
    
    # Filter by source if selected
    source_filter = request.GET.get('source')
    if source_filter:
        articles = articles.filter(source=source_filter)
    
    return render(request, 'news_app/dashboard.html', {
        'articles': articles,
        'sources': sources,
        'selected_source': source_filter
    })

def fetch_news(request):
    if request.method == 'POST':
        try:
            fetch_news_data()  # Fetch the latest news and save
            messages.success(request, "News updated successfully!")
        except Exception as e:
            messages.error(request, f"Error fetching news: {str(e)}")
    return redirect('dashboard')  # Or wherever your homepage is

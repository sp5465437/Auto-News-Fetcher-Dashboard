from datetime import datetime

def save_articles(self, articles):
    for article in articles:
        try:
            published_at_str = article.get('publishedAt')
            if published_at_str:
                published_at = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ")
            else:
                # fallback if missing
                published_at = datetime.now()

            NewsArticle.objects.create(
                title=article.get('title', 'No Title'),
                description=article.get('description', ''),
                url=article.get('url', ''),
                published_at=published_at,
                source=article['source']['name'] if article.get('source') else ''
            )
        except Exception as e:
            print(f"Error saving article: {e}")

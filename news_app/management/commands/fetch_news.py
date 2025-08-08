from django.core.management.base import BaseCommand
from news_app.services import fetch_news_articles

class Command(BaseCommand):
    help = 'Fetches latest news articles from NewsAPI'
    
    def handle(self, *args, **options):
        try:
            count = fetch_news_articles()
            self.stdout.write(self.style.SUCCESS(
                f'Successfully fetched {count} new articles'
            ))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Error fetching articles: {str(e)}'
            ))
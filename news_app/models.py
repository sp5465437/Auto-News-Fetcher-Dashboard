from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)  # <== this is probably missing
    url = models.URLField()
    published_at = models.DateTimeField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

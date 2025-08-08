from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('fetch-news/', views.fetch_news, name='fetch_news'),
]

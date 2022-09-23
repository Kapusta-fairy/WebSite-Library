from django.urls import path
from news.views import LatestNews

urlpatterns = [
    path('', LatestNews.as_view(), name='news'),
]

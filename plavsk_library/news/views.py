from django.views.generic import ListView
from news.models import News


class LatestNews(ListView):
    model = News

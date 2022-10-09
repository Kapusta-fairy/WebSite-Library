from django.views.generic import ListView
from content import news_title
from news.models import News


class LatestNews(ListView):
    paginate_by = 2
    model = News

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = news_title
        return context

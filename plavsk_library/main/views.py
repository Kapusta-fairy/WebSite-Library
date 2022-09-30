from django.views.generic import ListView
from content import main_title, main_content, main_name
from main.models import ImageLink


class ImageMain(ListView):
    model = ImageLink

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = main_title
        context['content'] = main_content
        context['main_name'] = main_name
        return context

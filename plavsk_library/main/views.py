from django.views.generic import ListView
from content import main_title, main_content
from main.models import ImageLink


class ImageMain(ListView):
    model = ImageLink

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = main_title
        context['content'] = main_content
        return context

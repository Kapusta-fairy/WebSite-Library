from django.views.generic import ListView
from content import MainTitle, MainContent
from main.models import ImageLink


class ImageMain(ListView):
    model = ImageLink

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Title'] = MainTitle
        context['Content'] = MainContent
        return context

from django.views.generic import ListView
from content import services_title
from services.models import Services


class FreeServices(ListView):
    model = Services

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = services_title
        return context

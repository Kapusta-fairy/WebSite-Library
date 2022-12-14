from django.views.generic import ListView
from content import history_title
from history.models import History


class ViewHistory(ListView):
    model = History

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = history_title
        return context

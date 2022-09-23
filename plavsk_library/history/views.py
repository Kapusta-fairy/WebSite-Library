from django.views.generic import ListView
from history.models import History


class ViewHistory(ListView):
    model = History

from django.views.generic import ListView
from content import dates_title
from dates.models import Dates, Years


class ViewDates(ListView):
    model = Dates

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = dates_title
        context['years'] = Years.objects.all()
        return context

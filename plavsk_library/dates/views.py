from django.views.generic import ListView
from dates.models import Dates


class ViewDates(ListView):
    model = Dates

from django.views.generic import ListView
from services.models import Services


class FreeServices(ListView):
    model = Services

from django.views.generic import ListView
from main.models import ImageLink


class ImageMain(ListView):
    model = ImageLink

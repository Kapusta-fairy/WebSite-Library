from django.views.generic import ListView
from documents.models import Documents


class ViewDocuments(ListView):
    model = Documents

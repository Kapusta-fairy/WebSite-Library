from django.views.generic import ListView
from content import documents_title
from documents.models import Documents


class ViewDocuments(ListView):
    model = Documents

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = documents_title
        return context

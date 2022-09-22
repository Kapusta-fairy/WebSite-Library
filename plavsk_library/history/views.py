from django.views.generic import ListView
from history.models import HistoryImageNoCaption, HistoryImageCaption, HistoryTextInfo


class ViewHistory(ListView):
    model = HistoryImageCaption
    template_name = 'history/history'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['HistoryImageNoCaption'] = HistoryImageNoCaption.objects.all()
        context['HistoryTextInfo'] = HistoryTextInfo.objects.all()
        return context

from django.contrib import admin
from history.models import HistoryImageNoCaption, HistoryImageCaption, HistoryTextInfo

admin.site.register(HistoryImageNoCaption)
admin.site.register(HistoryImageCaption)
admin.site.register(HistoryTextInfo)

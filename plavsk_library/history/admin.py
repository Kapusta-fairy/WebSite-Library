from django.contrib import admin
from django.utils.safestring import mark_safe
from history.models import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview')
    fields = ['name', 'image', 'preview', 'caption', 'text']
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 60px;">')

    preview.short_description = 'Миниатюра'


admin.site.register(History, HistoryAdmin)

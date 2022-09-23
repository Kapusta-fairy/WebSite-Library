from django.contrib import admin
from django.utils.safestring import mark_safe

from main.models import ImageLink


class MainAdmin(admin.ModelAdmin):
    list_display = ('preview', 'url')
    fields = ['image', 'preview', 'url']
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


admin.site.register(ImageLink, MainAdmin)
admin.site.site_header = 'Муниципальное бюджетное учреждение муниципального образования плавский район ' \
                         '"централизованная библиотечная система"'

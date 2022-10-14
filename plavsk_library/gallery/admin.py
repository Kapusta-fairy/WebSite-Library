from django.contrib import admin
from django.utils.safestring import mark_safe
from gallery.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('preview', 'image', 'name')
    fields = ['name', 'image', 'preview']
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 60px;">')

    preview.short_description = 'Миниатюра'


admin.site.register(Gallery, GalleryAdmin)

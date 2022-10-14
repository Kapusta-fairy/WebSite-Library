from django.contrib import admin
from django.utils.safestring import mark_safe
from structure.models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'preview')
    fields = ['title', 'department', 'text', 'photo', 'preview']
    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 60px;">')

    preview.short_description = 'Миниатюра'


admin.site.register(Staff, StaffAdmin)

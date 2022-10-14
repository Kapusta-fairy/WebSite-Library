from django.contrib import admin
from django.utils.safestring import mark_safe
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'prev_image1')
    fields = ['title', 'text', 'video', 'utube',
              'image1', 'prev_image1',
              'image2', 'prev_image2',
              'image3', 'prev_image3',
              'image4', 'prev_image4',
              'image5', 'prev_image5',
              'image6', 'prev_image6',
              'image7', 'prev_image7',
              'image8', 'prev_image8',
              'image9', 'prev_image9',
              'image10', 'prev_image10',
              'image11',  'prev_image11',
              'image12', 'prev_image12']
    readonly_fields = ['created_at',
                       'prev_image1', 'prev_image2', 'prev_image3', 'prev_image4', 'prev_image5', 'prev_image6',
                       'prev_image7', 'prev_image8', 'prev_image9', 'prev_image10', 'prev_image11', 'prev_image12']

    def prev_image1(self, obj):
        if obj.image1:
            return mark_safe(f'<img src="{obj.image1.url}" style="max-height: 60px;">')
    prev_image1.short_description = "Миниатюра 1"

    def prev_image2(self, obj):
        if obj.image2:
            return mark_safe(f'<img src="{obj.image2.url}" style="max-height: 60px;">')
    prev_image2.short_description = "Миниатюра 2"

    def prev_image3(self, obj):
        if obj.image3:
            return mark_safe(f'<img src="{obj.image3.url}" style="max-height: 60px;">')
    prev_image3.short_description = "Миниатюра 3"

    def prev_image4(self, obj):
        if obj.image4:
            return mark_safe(f'<img src="{obj.image4.url}" style="max-height: 60px;">')
    prev_image4.short_description = "Миниатюра 4"

    def prev_image5(self, obj):
        if obj.image5:
            return mark_safe(f'<img src="{obj.image5.url}" style="max-height: 60px;">')
    prev_image5.short_description = "Миниатюра 5"

    def prev_image6(self, obj):
        if obj.image6:
            return mark_safe(f'<img src="{obj.image6.url}" style="max-height: 60px;">')
    prev_image6.short_description = "Миниатюра 6"

    def prev_image7(self, obj):
        if obj.image7:
            return mark_safe(f'<img src="{obj.image7.url}" style="max-height: 60px;">')
    prev_image7.short_description = "Миниатюра 7"

    def prev_image8(self, obj):
        if obj.image8:
            return mark_safe(f'<img src="{obj.image8.url}" style="max-height: 60px;">')
    prev_image8.short_description = "Миниатюра 8"

    def prev_image9(self, obj):
        if obj.image9:
            return mark_safe(f'<img src="{obj.image9.url}" style="max-height: 60px;">')
    prev_image9.short_description = "Миниатюра 9"

    def prev_image10(self, obj):
        if obj.image10:
            return mark_safe(f'<img src="{obj.image10.url}" style="max-height: 60px;">')
    prev_image10.short_description = "Миниатюра 10"

    def prev_image11(self, obj):
        if obj.image11:
            return mark_safe(f'<img src="{obj.image11.url}" style="max-height: 60px;">')
    prev_image11.short_description = "Миниатюра 11"

    def prev_image12(self, obj):
        if obj.image12:
            return mark_safe(f'<img src="{obj.image12.url}" style="max-height: 60px;">')
    prev_image12.short_description = "Миниатюра 12"


admin.site.register(News, NewsAdmin)

from django.views.generic import ListView
from content import gallery_title
from gallery.models import Gallery


class ViewGallery(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gallery_title
        return context

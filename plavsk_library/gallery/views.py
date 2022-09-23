from django.views.generic import ListView
from gallery.models import Gallery


class ViewGallery(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'

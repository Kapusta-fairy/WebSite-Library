from django.urls import path
from gallery.views import ViewGallery

urlpatterns = [
    path('', ViewGallery.as_view(), name='gallery'),
]

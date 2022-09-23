from django.urls import path

from services.views import FreeServices

urlpatterns = [
    path('', FreeServices.as_view(), name='services'),
]

from django.urls import path
from main.views import ImageMain

urlpatterns = [
    path('', ImageMain.as_view(), name='main'),
]

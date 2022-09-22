from django.urls import path
from info.views import view_info

urlpatterns = [
    path('', view_info, name='info'),
]

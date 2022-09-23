from django.urls import path
from documents.views import ViewDocuments

urlpatterns = [
    path('', ViewDocuments.as_view(), name='documents'),
]

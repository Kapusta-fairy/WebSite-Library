from django.urls import path
from history.views import ViewHistory

urlpatterns = [
    path('', ViewHistory.as_view(), name='history'),
]

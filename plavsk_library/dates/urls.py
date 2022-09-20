from django.urls import path
from dates.views import ViewDates

urlpatterns = [
    path('', ViewDates.as_view(), name='dates'),
]

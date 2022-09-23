from django.urls import path
from structure.views import StaffStructure

urlpatterns = [
    path('', StaffStructure.as_view(), name='structure'),
]

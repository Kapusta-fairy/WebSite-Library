from django.urls import path
from info.views import OrganizationInfo

urlpatterns = [
    path('', OrganizationInfo.as_view(), name='info'),
]

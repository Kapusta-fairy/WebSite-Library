from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class ViewDatesTestCase(APITestCase):

    def test_200(self):
        url = reverse('dates')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

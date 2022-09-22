from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase


class ViewPagesTestCase(APITestCase):

    def test_dates(self):
        url = reverse('dates')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_documents(self):
        url = reverse('documents')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_gallery(self):
        url = reverse('gallery')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_history(self):
        url = reverse('history')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_info(self):
        url = reverse('info')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_main(self):
        url = reverse('main')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_news(self):
        url = reverse('news')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_services(self):
        url = reverse('services')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_structure(self):
        url = reverse('services')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

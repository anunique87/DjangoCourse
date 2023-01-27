from django.test import TestCase, Client
from django.urls import reverse
from booksinventory.models import Book
import json


class TestView(TestCase):
    def test_bookview(self):
        client = Client()
        response = client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)




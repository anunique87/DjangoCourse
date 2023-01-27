from django.test import SimpleTestCase
from django.urls import resolve, reverse
from booksinventory.views import BookView


class TestUrls(SimpleTestCase):
    def test_url_resolve(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func, BookView)

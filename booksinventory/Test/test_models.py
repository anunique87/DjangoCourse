from django.test import TestCase
from booksinventory.models import Book


class TestModels(TestCase):

    @staticmethod
    def create_book(idbook=1, nameofbook='Python', authorofbook='GuidoVanRossum', priceofbook=50):
        return Book.objects.create(idbook, nameofbook, authorofbook, priceofbook)

    def test_book(self):
        models = self.create_book()
        self.assertEqual(models.idbook, 1)

from django.test import TestCase
from booksinventory.models import Book


class TestBook(TestCase):
    def test_book(self):
        self.book1 = Book.objects.create(idbook=1, nameofbook='Python', authorofbook='GuidoVanRossum', priceofbook=190)

    def test_attribute(self):
        self.assertEqual(self.book1.idbook, 1)
        self.assertEqual(self.book1.nameofbook, 'Python')
        self.assertEqual(self.book1.authorofbook, 'GuidoVanRossum')
        self.assertEqual(self.book1.priceofbook, 190)

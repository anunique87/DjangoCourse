from django.test import TestCase
import pytest
from booksinventory.models import Animal


# class TestFunction:
#     def test_get(self):
#         pass
#
#     def test_post(self):
#         pass
#
#     def test_put(self):
#         pass
#
#     def test_delete(self):
#         pass


class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

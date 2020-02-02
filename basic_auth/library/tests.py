from django.test import TestCase

from library.models import Author


class TestModels(TestCase):

    def test_author(self):
        author = Author(name="Daniel Cow", contact="9879344")
        self.assertEqual(author.name, "Daniel Cow")
        self.assertEqual(author.contact, "9879344")
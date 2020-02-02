from django.test import TestCase

from library.models import Author, Publisher


class TestModel(TestCase):
    def test_author(self):
        author = Author(name="Gail Marker", contact="01893324")
        self.assertEqual(author.name, "Gail Marker")
        self.assertEqual(author.contact, "01893324")

    def test_publisher(self):
        publisher = Publisher(name="Dimik", contact="9823944")
        self.assertEqual(publisher.name, "Dimik")
        self.assertEqual(publisher.contact, "9823944")
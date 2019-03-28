from django.test import TestCase
from .models import Book

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title = "test1",
            slug = "test_1",
            description = "test 1 desc",
            releaseDate = "2010-03-12",
            author = "test1 Atuhot",
            genre = "test1 genre",
        )

    def testData(self):
        self.assertEqual(self.book.title,"test1")
        self.assertEqual(self.book.slug,"test_1")
        self.assertEqual(self.book.description,"test 1 desc")
        self.assertEqual(self.book.releaseDate,"2010-03-12")
        self.assertEqual(self.book.author,"test1 Atuhot")
        self.assertEqual(self.book.genre,"test1 genre")
        
    def testDb(self):
        book = Book.objects.get(slug = self.book.slug)
        self.assertEqual(self.book, book)
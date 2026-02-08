from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Tests CRUD operations, filtering, searching,
    ordering, and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data before each test runs.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.author = Author.objects.create(name="Chinua Achebe")

        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book.id}/"
        self.delete_url = f"/api/books/delete/{self.book.id}/"
        self.detail_url = f"/api/books/{self.book.id}/"

    # ------------------------
    # READ TESTS
    # ------------------------

    def test_get_book_list(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        """
        Test retrieving a single book by ID.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Things Fall Apart")

    # ------------------------
    # CREATE TESTS
    # ------------------------

    def test_create_book_requires_authentication(self):
        """
        Test that unauthenticated users cannot create books.
        """
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """
        Test that authenticated users can create books.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # ------------------------
    # UPDATE TESTS
    # ------------------------

    def test_update_book(self):
        """
        Test updating a book.
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": 1958,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Things Fall Apart (Updated)")

    # ------------------------
    # DELETE TESTS
    # ------------------------

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ------------------------
    # FILTER / SEARCH / ORDER TESTS
    # ------------------------

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get(self.list_url + "?publication_year=1958")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url + "?search=Fall")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        """
        Test ordering books by title.
        """
        response = self.client.get(self.list_url + "?ordering=title")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

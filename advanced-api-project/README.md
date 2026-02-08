## Book API Views

### Views Implemented
- BookListView: Retrieve all books (public access)
- BookDetailView: Retrieve a book by ID (public access)
- BookCreateView: Create a new book (authenticated users only)
- BookUpdateView: Update an existing book (authenticated users only)
- BookDeleteView: Delete a book (authenticated users only)

### Permissions
Read-only endpoints allow unauthenticated access.
Write operations require authentication.

### Validation
Custom validation is handled in BookSerializer to ensure
publication_year is not set in the future.


## Filtering, Searching, and Ordering

The BookListView supports advanced querying features.

### Filtering
Filter books by title, publication year, or author:
- /api/books/?publication_year=1958
- /api/books/?author=1

### Searching
Search books by title or author name:
- /api/books/?search=Achebe

### Ordering
Order results by title or publication year:
- /api/books/?ordering=title
- /api/books/?ordering=-publication_year

## API Testing

Unit tests are written in api/test_views.py using Django REST Framework's
APITestCase.

### What is Tested
- CRUD operations for Book endpoints
- Filtering, searching, and ordering
- Authentication and permission enforcement

### How to Run Tests
```bash
python manage.py test api


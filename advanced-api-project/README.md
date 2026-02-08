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

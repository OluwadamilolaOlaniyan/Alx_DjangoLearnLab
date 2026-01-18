

# CRUD Operations for Book model

## Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: Book object (1)>

## Retrieve
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

## Update
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four

## Delete
book = Book.objects.get(id=1)
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>

from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model represents a writer.
    One author can write many books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.
    Each book belongs to one author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


from django.shortcuts import render
#from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from django_filters import rest_framework
from rest_framework import generics
from rest_framework import filters
from .serializers import BookSerializer
from .models import Book

class BookListView(generics.ListAPIView):
    """Return a list of all books."""
    permission_classes = [IsAuthenticatedOrReadOnly]

    # filter_backends = [
    #     rest_framework.DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # ]
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["-publication_year"]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailView(generics.RetrieveAPIView):
    """Return details of a single book."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(generics.CreateAPIView):
    """Allow authenticated users to create a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookUpdateView(generics.UpdateAPIView):
    """Allow authenticated users to update a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    


class BookDeleteView(generics.DestroyAPIView):
    """Allow authenticated users to delete a book."""
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
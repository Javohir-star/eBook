from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from accounts.models import Book
from accounts.serializers import BookSerializer

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all().order_by('published_date')
    serializer_class = BookSerializer

class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.generics import ListAPIView
from accounts.models import User, Book
from accounts.serializers import UserSerializer, BookSerializer
from accounts.pagenation import CustomPagination 

class UserListView(ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = CustomPagination

class BookListView(ListAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    pagination_class = CustomPagination

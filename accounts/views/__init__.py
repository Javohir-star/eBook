from .book import (
    BookCreateAPIView,
    BookListAPIView,
    BookRetrieveAPIView,
    BookUpdateAPIView,
    BookDestroyAPIView
)
from .user import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView
)
from .token import MyTokenObtainPairView

__all__ = [
    'BookCreateAPIView',
    'BookListAPIView',
    'BookRetrieveAPIView',
    'BookUpdateAPIView',
    'BookDestroyAPIView',
    'UserCreateAPIView',
    'UserListAPIView',
    'UserRetrieveAPIView',
    'UserUpdateAPIView',
    'UserDestroyAPIView',
    'MyTokenObtainPairView',
]
from django.urls import path

from accounts.views import (
    UserCreateAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    BookCreateAPIView,
    BookListAPIView,
    BookRetrieveAPIView,
    BookUpdateAPIView,
    BookDestroyAPIView
)
from accounts.views.token import MyTokenObtainPairView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("accounts/user/create/", UserCreateAPIView.as_view(), name="user-create"),
    path(
        "accounts/user/list/",
        UserListAPIView.as_view(),
        name="user-list",
    ),
    path("accounts/user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user-retrieve"),
    path("accounts/user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user-update"),
    path("accounts/user/delete/<int:pk>/", UserDestroyAPIView.as_view(), name="user-delete"),
    
    path("accounts/book/create/", BookCreateAPIView.as_view(), name="book-create"),
    path(
        "accounts/book/list/",
        BookListAPIView.as_view(),
        name="book-list",
    ),
    path("accounts/book/<int:pk>/", BookRetrieveAPIView.as_view(), name="book-retrieve"),
    path("accounts/book/update/<int:pk>/", BookUpdateAPIView.as_view(), name="book-update"),
    path("accounts/book/delete/<int:pk>/", BookDestroyAPIView.as_view(), name="book-delete"),
]

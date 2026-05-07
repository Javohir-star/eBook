from accounts.models import User
from rest_framework import serializers
from .book import BookSerializer

class UserSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'books']
        read_only_fields = ['id']
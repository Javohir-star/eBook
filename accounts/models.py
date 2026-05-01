from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Book(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        "accounts.User", 
        on_delete=models.CASCADE, 
        related_name="books"
    )
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

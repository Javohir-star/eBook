from django.contrib import admin

from accounts.models import User, Book


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]
    search_fields = ["email", "name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "published_date"]
    search_fields = ["title"]
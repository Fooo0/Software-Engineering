# -*- coding: utf-8 -*-
from django.contrib import admin
from bookmanager.models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Name', 'AuthorID', 'Age', 'Country')

class BookAdmin(admin.ModelAdmin):
    list_display = ('Title', 'ISBN', 'AuthorID', 'Publisher', 'PublishDate', 'Price')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

from django.contrib import admin
from .models import Author, Book, Tag, Quote


@admin.register(Author, Book, Tag, Quote)
class PeopleAdmin(admin.ModelAdmin):
    pass

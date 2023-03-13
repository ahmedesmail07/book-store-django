from django.contrib import admin

# Register your models here.
from .models import Book  # Dot means that this models is in the same dir


class BookShow(admin.ModelAdmin):
    list_display = ("title", "author", "price")


admin.site.register(Book, BookShow)

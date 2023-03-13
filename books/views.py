from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"  # for making the varibale simple while looping
    template_name = "books/book_list.html"

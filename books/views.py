from django.shortcuts import render
from django.views.generic import *
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"  # for making the varibale simple while looping
    template_name = "books/book_list.html"

class BookDetailView(DetailView):
    # We can also use the qs for retrieve all the data from the MODEL
    queryset = Book.objects.all()
    context_object_name = "book_detail"
    template_name = "books/book_detail.html"
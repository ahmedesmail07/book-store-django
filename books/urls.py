from django.urls import path
from .views import *


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    # Adding Individual page for each book :
    path("<uuid:pk>/",BookDetailView.as_view(),name="book_detail") ,
]

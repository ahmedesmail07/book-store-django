from django.db import models
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    #thic can be used easily for refering for a specific book.id in urls
    def get_absolute_url(self):
        return reverse("book_detail",args=[str(self.id)])
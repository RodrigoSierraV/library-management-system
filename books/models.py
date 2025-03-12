from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

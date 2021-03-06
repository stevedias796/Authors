from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Books(models.Model):
    book_name = models.ForeignKey(Author, on_delete= models.CASCADE)

    def __str__(self):
        return self.book_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_names = models.CharField(max_length=200)

    def __str__(self):
        return self.book_names
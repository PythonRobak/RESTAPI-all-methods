from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title



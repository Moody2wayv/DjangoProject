from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField()
    signature = models.CharField(max_length=140, default="Mr M")  # Added default parameter

    def __str__(self):
     return self.title  


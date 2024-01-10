from django.db import models
from main.models.Person import Person

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(Person,on_delete=models.CASCADE)
    
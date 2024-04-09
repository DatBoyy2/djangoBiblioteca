from django.db import models

# Create your models here.

class Autor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Editorial(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Tema(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Autor)
    editorial = models.ManyToManyField(Editorial)
    year = models.PositiveIntegerField()
    theme = models.ManyToManyField(Tema)
    ISBN = models.CharField(max_length=20)
    SBM = models.CharField(max_length=20)
    plot = models.TextField()
    img = models.ImageField(upload_to='media',blank=True, null=True)
    def __str__(self):
        return self.title
    
from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

# Create your models here.

class Movie(models.Model):
    isim = models.CharField(max_length = 100)
    resim = models.FileField(upload_to= 'filmler/', null = True)


    def __str__(self):
        return self.isim

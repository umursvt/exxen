from email import message
from django.shortcuts import render
from .models import *


# Create your views here.

def index(requests):
    filmler = Movie.objects.all()
    context = {
        'filmler': filmler
    }
    return render(requests,'index.html',context)


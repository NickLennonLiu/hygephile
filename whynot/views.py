from django.shortcuts import render
from .models import Category, Dos
# Create your views here.


def index(request):
    cats = Category.objects.all()

    return render(request, 'whynot/whynot.html', {"content": cats})


from django.shortcuts import render
from .models import FeelLikeIt
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse(FeelLikeIt.objects.count())


def commit_your_crime(request):
    pass

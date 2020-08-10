from django.shortcuts import render
from .models import FeelLikeIt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse(FeelLikeIt.objects.count())


def new(request):
    if request.method == "GET":
        return render(request, 'feellikeit/new.html')
    if request.method == "POST":
        date = request.POST.get("date")
        reason = request.POST.get("reason")
        snap = request.FILES.get("snap")
        no = request.POST.get("no")
        FeelLikeIt.objects.create(date=date, reason=reason, snap=snap, no=no)
        return HttpResponseRedirect(reverse('index'))

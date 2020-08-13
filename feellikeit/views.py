from django.shortcuts import render
from .models import FeelLikeIt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    times = FeelLikeIt.objects.count()
    last_time = FeelLikeIt.objects.last().date
    content = {
        "times": times,
        "last_time": last_time,
    }
    return render(request, 'feellikeit/statics.html', content)


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

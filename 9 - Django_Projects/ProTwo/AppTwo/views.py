from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<em>My Second App<em>")


def help_me(request):
    context = {'help_me': "Help Page"}
    return render(request, 'apptwo/help.html', context)
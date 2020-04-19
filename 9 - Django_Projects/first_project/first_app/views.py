from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me':"Hello! Now I am coming from first_app/index.html"}
    return render(request, 'first_app/index.html', my_dict)  # context=my_dict


def first_app(request):
    return HttpResponse("<h1>This is my first App!!</h1>")
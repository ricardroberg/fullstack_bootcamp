from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {'insert_content': "HELLO IM FROM THIRD APP"}
    return render(request, 'third_app/index.html', context)


def third_app(request):
    return HttpResponse('<h1>This is the Third App Page!</h1>')
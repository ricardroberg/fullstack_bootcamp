from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Webpage, AccessRecord, Users
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', date_dict)  # context=my_dict


def users(request):
    user_list = Users.objects.order_by('first_name')
    context = {'users': user_list}
    return render(request, 'users/users.html', context)

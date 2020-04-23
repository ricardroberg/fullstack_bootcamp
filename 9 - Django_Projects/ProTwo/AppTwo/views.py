from django.shortcuts import render
# from django.http import HttpResponse
from .models import User
from .forms import SignIn

# Create your views here.


def index(request):
    return render(request, 'apptwo/index.html')


def help_me(request):
    context = {'help_me': "Help Page"}
    return render(request, 'apptwo/help.html', context)


def users(request):
    user_list = User.objects.order_by('first_name')
    context = {'users': user_list}
    return render(request, 'apptwo/users.html', context)


def signin(request):

    form = SignIn()

    if request.method == 'POST':
        form = SignIn(request.POST)

        if form.is_valid():
            # fname = form.cleaned_data['first_name']
            # lname = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # s = Accounts(first_name=fname, last_name=lname, email=email)
            # s.save()
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')


    return render(request, 'apptwo/signin.html', {'form': form})

from django.urls import path
from .views import index, help_me, users, signin

urlpatterns = [
    path('', index, name='index'),
    path('help/', help_me, name='help'),
    path('users/', users, name='users'),
    path('signin/', signin, name='signin')
]

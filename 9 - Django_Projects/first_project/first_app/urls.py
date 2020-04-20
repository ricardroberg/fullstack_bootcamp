from django.urls import path, include
from .views import index, users

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users')
]

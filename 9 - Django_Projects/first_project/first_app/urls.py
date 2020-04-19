from django.urls import path, include
from .views import index, first_app

urlpatterns = [
    path('', index, name='index'),
    path('first_app/', first_app, name='first_app')
]

from django.urls import path, include
from .views import index, third_app

urlpatterns = [
    path('', index, name='index'),
    path('third_app/', third_app, name='third_app')
]
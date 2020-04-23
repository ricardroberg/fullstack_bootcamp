from django.urls import path, include
from .views import index, form_name_view

urlpatterns = [
    path('', index, name='index'),
    path('formpage/', form_name_view, name='form_name')
]
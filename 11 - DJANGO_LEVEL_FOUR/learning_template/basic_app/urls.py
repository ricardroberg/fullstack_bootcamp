from django.urls import path
from .views import index, other, relative

app_name = 'basic_app'  # To be used in HTML {% url 'basic_app:relative %}

urlpatterns = [
    path('relative/', relative, name='relative'),
    path('other/', other, name='other')
]

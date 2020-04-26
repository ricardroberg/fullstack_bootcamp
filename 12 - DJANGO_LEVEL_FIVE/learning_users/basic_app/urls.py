from django.urls import path
from .views import basic_app_index, register, user_logout, special, user_login

app_name = 'basic_app'

urlpatterns = [
    path('', basic_app_index, name='basic_app_index'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('special/', special, name='special'),
    path('user_login/', user_login, name='user_login'),
]
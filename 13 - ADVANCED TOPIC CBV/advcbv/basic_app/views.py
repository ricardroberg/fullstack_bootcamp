from django.shortcuts import render
from django.views.generic import (View,
                                  TemplateView,
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list.html endereço baseado na classe
    # return school_list if context_object_name not defined


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    # template_name = 'basic_app/school_detail.html' # school_detaul.html address basded on class name?
    # return school if context_object_name not defined


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model= models.School
    success_url = reverse_lazy("basic_app:list")


# TEST VIEW
class MyDogListView(ListView):
    context_object_name = 'my_dogs'
    model = models.MyDog

# class IndexView(TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context

# # CLASS BASED VIEWS
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")

# BASIC VIEW
# def index(request):
#     return render(request, 'index.html')


# <!--                {% if user.is_authenticated %}-->
# <!--                    <li class="nav-item">-->
# <!--                        <a class="nav-link" href="{% url 'basic_app:logout' %}">Logout</a>-->
# <!--                        </li>-->
# <!--                {% else %}-->
# <!--                    <li class="nav-item">-->
# <!--                        <a class="nav-link" href="{% url 'basic_app:user_login' %}">Login</a>-->
# <!--                        </li>-->
# <!--                {% endif %}-->
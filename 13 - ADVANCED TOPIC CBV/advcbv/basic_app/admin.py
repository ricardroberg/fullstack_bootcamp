from django.contrib import admin
from .models import School, Student, MyDog


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'principal', 'location')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'school')


class MyDogAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'age')


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(MyDog, MyDogAdmin)

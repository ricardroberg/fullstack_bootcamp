from django.contrib import admin
from . import models


class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'release_year', 'length']

    search_fields = ['title', 'release_year']

    list_filter = ['release_year']

    list_display = ['title', 'release_year', 'length']

    list_editable = ['length']


class CustomerAdmin(admin.ModelAdmin):
    fields = ['phone', 'last_name', 'first_name']

    search_fields = ['phone', 'last_name', 'first_name']

    # list_filter = ['last_name']

    list_display = ['last_name', 'first_name', 'phone']


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Movie, MovieAdmin)

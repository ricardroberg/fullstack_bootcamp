from django.contrib import admin
from .models import AccessRecord, Topic, Webpage, Users

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)


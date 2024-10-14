from django.contrib import admin

# Register your models here.
from . models import User,Area,Grievance

admin.site.register(User)
admin.site.register(Area)
admin.site.register(Grievance)
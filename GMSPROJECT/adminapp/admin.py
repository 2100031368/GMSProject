from django.contrib import admin

# Register your models here.
from . models import User,Area,Grievance,EditData, About, Contact, Usage, Notification

admin.site.register(User)
admin.site.register(Area)
admin.site.register(Grievance)
admin.site.register(EditData)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Usage)
admin.site.register(Notification)
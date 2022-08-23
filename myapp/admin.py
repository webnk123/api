from django.contrib import admin
from .models import Client, Mailinglist, Messagetosend

# Register your models here.

admin.site.register(Client)
admin.site.register(Mailinglist)
admin.site.register(Messagetosend)
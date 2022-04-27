from django.contrib import admin

# Register your models here.
from .models import Useragreement, User_mail

admin.site.register(User_mail)
admin.site.register(Useragreement)
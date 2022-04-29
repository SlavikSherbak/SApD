from django.contrib import admin

# Register your models here.
from .models import Useragreement, User_mail, User_telegram, Telegram_group

admin.site.register(Telegram_group)
admin.site.register(User_telegram)
admin.site.register(User_mail)
admin.site.register(Useragreement)
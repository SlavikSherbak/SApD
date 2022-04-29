from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse

from login.models import Useragreement, User_mail, User_telegram, Telegram_group

#def useragreement(request):
    #useragreement = Useragreement.objects.all()
    #return render(request, 'login/list.html', {'useragreement': useragreement})

def main(request):
    return render(request, 'login/index.html')

def login_key(request):
    return render(request, 'login/login_key.html')

def email_login(request):
    a = User_mail(user_mail = request.POST['user_mail'], user_mail_sender = request.POST['mail_sender'])
    a.save()

    telegram_group = Telegram_group.objects.all()
    useragreement = Useragreement.objects.all() 
    return render(request, 'login/license.html', {'telegram_group': telegram_group, 'useragreement': useragreement})

def telegram_login(request):
    a = User_telegram(user_telegram = request.POST['user_telegram'])
    a.save()
    telegram_group = Telegram_group.objects.all()
    useragreement = Useragreement.objects.all() 
    return render(request, 'login/license.html', {'telegram_group': telegram_group, 'useragreement': useragreement})

def login(request):
    return render(request, 'login/login.html')

    
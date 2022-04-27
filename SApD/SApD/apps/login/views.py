from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.urls import reverse

from login.models import Useragreement, User_mail

#def useragreement(request):
    #useragreement = Useragreement.objects.all()
    #return render(request, 'login/list.html', {'useragreement': useragreement})

def main(request):
    return render(request, 'login/index.html')

def login_key(request):
    return render(request, 'login/login_key.html')

def user_mail(request):
    
    a = User_mail(user_mail = request.POST['name'], user_mail_sender = request.POST['mail_sender'])
    a.save()
    

    return render(request, 'login/login.html')

def login(request):
    return render(request, 'login/login.html')

def license(request):
    useragreement = Useragreement.objects.get(id = 1)
    return render(request, 'login/license.html', {'useragreement': useragreement})
    
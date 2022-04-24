from django.shortcuts import render
from .models import Useragreement

#def useragreement(request):
    #useragreement = Useragreement.objects.all()
    #return render(request, 'login/list.html', {'useragreement': useragreement})

def main(request):
    return render(request, 'login/index.html')

def login_key(request):
    return render(request, 'login/login_key.html')

def login(request):
    return render(request, 'login/login.html')

def license(request):
    useragreement = Useragreement.objects.all()
    return render(request, 'login/license.html', {'useragreement': useragreement})
    
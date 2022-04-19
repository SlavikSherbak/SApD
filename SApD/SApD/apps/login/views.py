from django.shortcuts import render
from .models import Useragreement

#def useragreement(request):
    #useragreement = Useragreement.objects.all()
    #return render(request, 'login/list.html', {'useragreement': useragreement})

def login(request):
    return render(request, 'login/index.html')
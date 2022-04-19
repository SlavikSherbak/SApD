from django.shortcuts import render
from .models import Useragreement

def index(request):
    useragreement = Useragreement.objects.all()
    return render(request, 'login/list.html', {'useragreement': useragreement})
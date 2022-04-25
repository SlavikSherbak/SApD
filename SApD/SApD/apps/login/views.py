from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import BadHeaderError,send_mail

from .models import Useragreement
from .forms import NameForm

#def useragreement(request):
    #useragreement = Useragreement.objects.all()
    #return render(request, 'login/list.html', {'useragreement': useragreement})

def main(request):
    return render(request, 'login/index.html')

def login_key(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['your_name']

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'login/login_key.html', {'form': form})

def login(request):
    return render(request, 'login/login.html')

def license(request):
    useragreement = Useragreement.objects.all()
    return render(request, 'login/license.html', {'useragreement': useragreement})
    
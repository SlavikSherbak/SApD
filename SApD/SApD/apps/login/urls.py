from django.urls import path

from . import views

urlpatterns = [
    #path('', views.useragreement, name = 'login'),
    path('', views.login, name = 'login')
]
from django.urls import path

from . import views

urlpatterns = [
    #path('', views.useragreement, name = 'login'),
    path('login', views.login),
    path('license', views.license),
    path('login_key', views.login_key),
    path('', views.main),
    
]
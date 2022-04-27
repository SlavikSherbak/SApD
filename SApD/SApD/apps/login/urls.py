from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    #path('', views.useragreement, name = 'login'),
    path('user_mail', views.user_mail, name = 'user_mail'),
    path('login', views.login),
    path('license', views.license),
    path('login_key', views.login_key),
    path('', views.main),
    
]
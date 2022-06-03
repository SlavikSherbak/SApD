from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    #path('', views.useragreement, name = 'login'),
    path('registration/instruction', views.instruction, name = 'instruction'),
    path('registration/telegram_login', views.telegram_login, name = 'telegram_login'),
    path('registration/email_login', views.email_login, name = 'email_login'),
    path('login', views.login, name = 'login'),
    path('registration/login_key', views.login_key, name = 'login_key'),
    path('', views.main, name = 'main'),
]

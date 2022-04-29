from django.urls import path

from . import views

app_name = 'messenger'
urlpatterns = [
    path('', views.main, name = 'main'),
    
]
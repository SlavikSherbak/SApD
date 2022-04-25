from django.db import models

# Create your models here.
class Useragreement(models.Model):
    useragreement_text = models.TextField('Текст лицензионого соглашения')

    def __str__(self):
        return self.useragreement_text

    class Meta:
        verbose_name = 'Соглашение'
        verbose_name_plural = 'Соглашения'

class User_mail(models.Model):
    user_mail = models.CharField('Почта пользователя', max_length = 200)

    def __str__(self):
        return self.user_mail
    
    class Meta:
        verbose_name = 'Почта пользователя'
        verbose_name_plural = 'Почты пользователей'
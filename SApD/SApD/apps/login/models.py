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
    user_mail = models.CharField('Почта пользователя', max_length = 100)
    user_mail_sender = models.CharField('Почта для отправителя пользователя', max_length = 100, default = 'sapdloginkey@gmail.com')

    def __str__(self):
        return self.user_mail
    
    class Meta:
        verbose_name = 'Почта пользователя'
        verbose_name_plural = 'Почты пользователей'


class Telegram_group(models.Model):
    user_telegram_sender = models.CharField('Телеграм группа с кодами', max_length = 100)

    def __str__(self):
        return self.user_telegram_sender

    class Meta:
        verbose_name = 'Телеграм группа с кодом доступа'
        verbose_name_plural = 'Телеграм группа с кодами'

class User_telegram(models.Model):
    user_telegram = models.CharField('Телеграм пользователя', max_length = 100)

    def __str__(self):
        return self.user_telegram
    
    class Meta:
        verbose_name = 'Телеграм пользователя'
        verbose_name_plural = 'Телеграмы пользователей'
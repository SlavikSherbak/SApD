# Generated by Django 4.0.3 on 2022-04-27 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_user_mail_user_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_mail',
            name='user_telegram',
        ),
        migrations.AddField(
            model_name='user_mail',
            name='user_mail_sender',
            field=models.CharField(default='sapdloginkey@gmail.com', max_length=100, verbose_name='Почта для отправителя пользователя'),
        ),
    ]
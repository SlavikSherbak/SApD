# Generated by Django 4.0.3 on 2022-04-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_user_mail_options_alter_user_mail_user_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_mail',
            name='user_telegram',
            field=models.CharField(default='text', max_length=100, verbose_name='Почта пользователя'),
        ),
    ]

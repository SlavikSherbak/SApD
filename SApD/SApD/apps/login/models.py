from django.db import models

# Create your models here.
class Useragreement(models.Model):
    useragreement_text = models.TextField('Текст лицензионого соглашения')

    def __str__(self):
        return self.useragreement_text

    class Meta:
        verbose_name = 'Соглашение'
        verbose_name_plural = 'Соглашения'
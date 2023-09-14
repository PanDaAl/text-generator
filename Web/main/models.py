from django.db import models


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.CharField('Email-адрес', max_length=30)
    text = models.CharField('Сообщение', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
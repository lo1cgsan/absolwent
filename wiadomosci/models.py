from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Wiadomosc(models.Model):
    tresc = models.TextField("treść wiadomości")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_d = models.DateTimeField("dodana", default=timezone.now)

    class Meta:
        verbose_name = 'wiadomość'
        verbose_name_plural = 'wiadomości'
        ordering = ['-data_d',]

    def wiadomosc_skrot(self):
        return self.tresc[0:40]

    def __str__(self):
        return self.tresc[0:40] + '(' + '{0:%Y-%m-%d %H:%M:%S}'.format(self.data_d) + ')'

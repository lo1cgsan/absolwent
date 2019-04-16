from django.db import models
from django.utils import timezone


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'kategorie'

    def __str__(self):
        return self.nazwa


class Pytanie(models.Model):
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, blank=True, null=True, related_name="pytania")
    tekst_pytania = models.CharField('tekst pytania', max_length=200)
    data_d = models.DateTimeField('data dodania', default=timezone.now)

    class Meta:
        verbose_name_plural = 'pytania'
        ordering = ['-data_d', ]

    def __str__(self):
        return self.tekst_pytania[0:50]


class Odpowiedz(models.Model):
    pytanie = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    tekst_odpowiedzi = models.CharField('tekst odpowiedzi', max_length=200)
    glosy = models.IntegerField('liczba głosów', default=0)

    class Meta:
        verbose_name_plural = 'odpowiedzi'

    def __str__(self):
        return self.tekst_odpowiedzi[0:50]
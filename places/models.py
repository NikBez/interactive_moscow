from django.db import models

class Place(models.Model):
    title = models.CharField("Название", max_length=100)
    short_description = models.CharField("Краткое описание", max_length=300, blank=True)
    long_description = models.TextField("Полное описание", blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


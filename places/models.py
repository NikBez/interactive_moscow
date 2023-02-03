from django.db import models

class Place(models.Model):
    title = models.CharField("Название", max_length=100)
    images = models.ManyToManyField("Image", verbose_name="Изображение", blank=True, related_name="places")
    short_description = models.CharField("Краткое описание", max_length=300, blank=True)
    long_description = models.TextField("Полное описание", blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField("Картинка", upload_to="places/")




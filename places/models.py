from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField("Название", max_length=100)
    images = models.ManyToManyField("Image",
                                    verbose_name="Изображение",
                                    blank=True,
                                    related_name="places",
                                    through='ImagesPlace'
                                    )
    short_description = models.CharField("Краткое описание",
                                         max_length=300,
                                         blank=True
                                         )
    long_description = tinymce_models.HTMLField("Полное описание",
                                                blank=True
                                                )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField("Картинка", upload_to="places/")

    def __str__(self):
        return self.image.name


class ImagesPlace(models.Model):
    """
    This is a junction table model that also stores
    the images order for a place.
    """
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, models.CASCADE)
    images_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['images_order']

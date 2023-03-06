from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):

    title = models.CharField('Название', max_length=100)
    short_description = models.TextField(
        'Краткое описание',
        blank=True,
    )
    long_description = tinymce_models.HTMLField(
        'Полное описание',
        blank=True,
    )
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Картинка', upload_to='places/')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        null=True,
        related_name='images'
    )
    my_order = models.PositiveIntegerField(
        db_index=True,
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return self.image.name

from django.contrib import admin
from places.models import Place, Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat', 'short_description')
    fields = ('title', ('lng', 'lat'), 'short_description', 'long_description', 'images')
    filter_horizontal = ['images']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

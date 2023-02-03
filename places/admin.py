from django.contrib import admin
from places.models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat', 'short_description')
    fields = ('title', ('lng', 'lat'), 'short_description', 'long_description')


from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class PreviewMixin:

    def preview(self, img):
        return format_html(
            '<img src="{url}" style= "max-width: 200px; height: auto;" />',
            url=img.image.url,
            width=200,
            height=200
        )


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline, PreviewMixin):
    model = Image
    fields = ['image', 'preview']
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    extra = 0
    readonly_fields = ['preview']


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat', 'short_description')
    fields = ('title', ('lng', 'lat'), 'short_description', 'long_description',)
    inlines = [ImagesInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, PreviewMixin):
    fields = ['image', 'place', 'preview']
    readonly_fields = ['preview']

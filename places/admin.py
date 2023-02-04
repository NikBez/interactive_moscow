from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from places.models import Place, Image


class ImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Place.images.through
    fields = ['image', 'preview']
    verbose_name = "Изображения"
    verbose_name_plural = "Изображения"
    extra = 0
    readonly_fields = ('preview',)

    def preview(self, obj):

            image = Image.objects.get(id=obj.image_id)
            height, width = downscale_image(image.image.height, image.image.width)
            return format_html('<img src="{url}" width="{width}" height={height} />'.format(
                url=image.image.url,
                width=width,
                height=height,
            )
            )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat', 'short_description')
    fields = ('title', ('lng', 'lat'), 'short_description', 'long_description',)
    inlines = [
        ImagesInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['preview']
    readonly_fields = ["preview"]
    exclude = ['image']

    def preview(self, obj):
        height, width = downscale_image(obj.image.height, obj.image.width)
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,
            height=height,
        )
        )

def downscale_image(heigth, width):
    prop = width/200
    return heigth/prop, 200

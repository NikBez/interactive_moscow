# Generated by Django 3.0 on 2023-03-03 02:49

from django.db import migrations

# from places.models import Image, ImagesPlace


# def relocatePlaces(apps, schema_editor):
#     source_images = ImagesPlace.objects.all()
#     for source_image in source_images:
#         image = Image.objects.get(pk=source_image.pk)
#         image.place = source_image.place
#         image.save()

def move_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20230303_0249'),
    ]
    operations = [
        # migrations.RunPython(relocatePlaces, reverse_code=move_backward)
    ]

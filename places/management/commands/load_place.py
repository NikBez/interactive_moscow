import sys
import requests

from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = "Load places from json files"

    def handle(self, *args, **options):
        response = requests.get(args[0])
        response.raise_for_status()
        response = response.json()
        try:
            lng = float(response['coordinates']['lng'])
            lat = float(response['coordinates']['lat'])
        except ValueError('Coordinates does not correct'):
            sys.exit()

        place, created = Place.objects.get_or_create(
            title=response['title'],
            short_description=response['description_short'],
            long_description=response['description_long'],
            lng=lng,
            lat=lat
            )

        if created:
            image_urls = [img_url for img_url in response['imgs']]
            for url in image_urls:
                img_name = url.split('/')[-1]
                response = requests.get(url)
                response.raise_for_status()
                cur_image = Image(place=place)
                cur_image.image.save(img_name, ContentFile(response.content))
        else:
            print('This place is already exist.')

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='+',
            type=str,
            dest='args'
        )

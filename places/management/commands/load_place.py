import sys

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places from json files'

    def handle(self, *args, **options):
        response = requests.get(options['url_to_json'])
        response.raise_for_status()
        response = response.json()
        lng = float(response['coordinates']['lng'])
        lat = float(response['coordinates']['lat'])

        place, created = Place.objects.get_or_create(
            title=response['title'],
            lng=lng,
            lat=lat,
            defaults={
                'short_description': response.get('description_short', ''),
                'long_description': response.get('description_long', ''),
            }
        )
        if created:
            image_urls = [img_url for img_url in response.get('imgs', [])]
            for url in image_urls:
                img_name = url.split('/')[-1]
                response = requests.get(url)
                response.raise_for_status()
                image = Image(place=place)
                image.image.save(img_name, ContentFile(response.content))
        else:
            print('This place is already exist.')

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            type=str,
            dest='url_to_json'
        )

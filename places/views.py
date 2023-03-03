import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe

from places.models import Place


def view_main_page(request):

    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': reverse('places', kwargs={'id': place.id}),
            }
        })

    context = {
        'geo': {
            'type': 'FeatureCollection',
            'features': features,
        },
    }

    return render(request, 'places/index.html', context=context)


def place_page_view(request, id):

    place = get_object_or_404(Place, id=id)
    place_detales = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
            }
        }
    return JsonResponse(place_detales, json_dumps_params={'ensure_ascii': False})

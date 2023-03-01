import json

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.safestring import mark_safe

from places.models import Place


def main_page_view(request):

    places = Place.objects.all()

    geo = {"type": "FeatureCollection", "features": []}
    for place in places:
        geo["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse('places', kwargs={'id': place.id}),
            }
        })
    context = {
        "geo": geo,
    }

    return render(request, "places/index.html", context=context)

def place_page_view(request, id):

    place = get_object_or_404(Place, id=id)
    place_detales = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
            }
        }
    context = {
        'json': mark_safe(json.dumps(place_detales, ensure_ascii=False, indent=4)),
    }
    return render(request, "places/place.html", context=context)

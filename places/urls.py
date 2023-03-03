from django.urls import path
from places.views import view_main_page, place_page_view

urlpatterns = [
    path('', view_main_page, name='main'),
    path('places/<int:id>/', place_page_view, name='places')
]

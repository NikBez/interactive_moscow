from django.urls import path
from interactive_map.views import main_page_view

urlpatterns = [
    path('', main_page_view, name='main'),
]
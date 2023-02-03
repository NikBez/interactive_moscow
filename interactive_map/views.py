from django.shortcuts import render
from django.http.response import HttpResponse


def main_page_view(request):
    return render(request, "interactive_map/main.html")


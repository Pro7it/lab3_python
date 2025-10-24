from django.http import HttpResponse
from django.shortcuts import render
from .repository.MainPoint import MainPoint

# Create your views here.
def theatre_view(request):
    return HttpResponse(MainPoint().theaters.get_by_id(request.GET.get('id')))

def play_view(request):
    return HttpResponse(MainPoint().plays.get_by_id(request.GET.get('id')))

def genre_view(request):
    return HttpResponse(MainPoint().genres.get_all())
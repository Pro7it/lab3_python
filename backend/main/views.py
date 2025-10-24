from django.http import HttpResponse
from django.shortcuts import render
from .repository.MainPoint import MainPoint

# Create your views here.
def get(request, model_name):
    mp = MainPoint()

    if not hasattr(mp, model_name): return HttpResponse(f"Error: repository '{model_name}' not found")

    repository = getattr(mp, model_name)
    item_id = request.GET.get('id')

    if item_id: return HttpResponse(str(repository.get_by_id(item_id)))
    else: return HttpResponse(str(repository.get_all()))
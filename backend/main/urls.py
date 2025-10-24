from django.urls import path
from .views import *

urlpatterns = [
    path('theatre/', theatre_view, name='theatre'),
    path('play/', play_view, name='play'),
    path('genre/', genre_view, name='genre'),
]
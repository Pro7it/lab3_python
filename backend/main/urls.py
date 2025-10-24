from django.urls import path
from .views import *

urlpatterns = [
    path('<str:model_name>', get, name='get'),
]
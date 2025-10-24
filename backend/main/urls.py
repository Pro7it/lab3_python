from django.urls import path
from .views import *

urlpatterns = [
    path('<str:model_name>', get),
    path('<str:model_name>/add', add),
]
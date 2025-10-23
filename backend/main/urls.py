from django.urls import path
from . import views

urlpatterns = [
    path('director/read', views.read, name='test'),
    path('director/add', views.add, name='test'),
]
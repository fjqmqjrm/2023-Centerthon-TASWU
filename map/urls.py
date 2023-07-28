from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_main, name='map_main'),
]
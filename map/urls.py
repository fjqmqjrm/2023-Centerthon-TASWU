from django.urls import path
from . import views
app_name = 'map'
urlpatterns = [
    path('', views.map_main, name='map_main'),
    #path('custom_logout/', views.custom_logout, name='custom_logout'),
]
from django.urls import path
from . import views
app_name = 'map'
urlpatterns = [
    path('', views.map_main, name='map_main'),
    path('search', views.map_search, name='map_search'),
    #path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('station_add_turn/', views.station_add_turn, name='station_add_turn'),
    path('station_add/', views.station_add, name='station_add'),
    path('call/', views.map_call, name='map_call'),
    path('notifications/', views.TaxiCallListView.as_view(), name='taxi-call-list'),
]
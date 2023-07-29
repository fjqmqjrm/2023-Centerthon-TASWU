from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('mypage/', views.my_page, name='my_page'),
    ]
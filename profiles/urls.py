from django.urls import path
from . import views
app_name = 'profiles'
urlpatterns = [
    path('', views.start_login, name='main_login'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),
    path('mypage/', views.my_page, name='my_page'),
    path('call_list/', views.call_list, name='call_list'),
    path('update_profile_image/', views.update_profile_image, name='update_profile_image'),
    path('phone_number/', views.phone_number, name='phone_number'),
    path('coin/', views.coin, name='coin'),
    path('service/', views.service, name='service'),
    ]
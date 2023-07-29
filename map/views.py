from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
def map_main(request):
    return render(request, 'map/kakao_map.html')



def custom_logout(request):
    logout(request)
    return redirect('map_main')
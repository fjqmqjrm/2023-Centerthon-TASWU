from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from profiles.models import Station
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def map_main(request):
    user_profile = None
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_profile = request.user.userprofile

    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'map/kakao_map.html', context)



def custom_logout(request):
    logout(request)
    return redirect('map_main')

def map_search(request):
    return render(request, 'map/map_search.html')



@login_required
def station_add_turn(request):

    return render(request, 'map/kakao_map_station_add.html')



@login_required
def station_add(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        UserProfile  = request.user.userprofile
        # Station 객체 생성과 저장
        new_station = Station(address=address, name="승강장 이름을 설정해주세요.", UserProfile = UserProfile )
        new_station.save()

    return render(request, 'map/kakao_map.html')


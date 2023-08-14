from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from profiles.models import Station, TaxiCall
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def map_main(request):
    user_profile = None
    user_stations = []
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_profile = request.user.userprofile
        user_stations = user_profile.station_set.all()  # 현재 사용자의 연결된 Station들을 가져옴

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_stations': user_stations,
    }
    if request.user.userprofile.is_taxi_driver:  # 현재 사용자의 is_taxi_driver 값을 확인
        return render(request, 'map/taxi_driver_page.html', context)
    else: #코인 적립 및 택시 호출 구분
        if request.method == 'POST':            
            user_profile.coins += 1
            user_profile.save()
            #받아온 주소값
            address = request.POST.get('address')
            # TaxiCall 객체 생성 및 저장
            taxi_call = TaxiCall(client=user_profile, address=address)
            taxi_call.save()
            
            return redirect('map:map_call')
        return render(request, 'map/kakao_map.html', context)

def custom_logout(request):
    logout(request)
    return redirect('map_main')

def map_search(request):
    return render(request, 'map/map_search.html')

@login_required
def station_add_turn(request):
    if request.user.is_authenticated and hasattr(request.user, 'userprofile'):
        user_profile = request.user.userprofile
        user_stations = user_profile.station_set.all()  # 현재 사용자의 연결된 Station들을 가져옴           

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'user_stations': user_stations,
    }
    return render(request, 'map/kakao_map_station_add.html', context)

@login_required
def station_add(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        name = request.POST.get('station_name')
        UserProfile  = request.user.userprofile
        UserProfile.coins -= 2
        UserProfile.save()
        # Station 객체 생성과 저장
        new_station = Station(address=address, name=name, UserProfile = UserProfile )
        new_station.save()
        return redirect('map:map_main')

@login_required
def map_call(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        user_profile = request.user.userprofile

        # Update the user's current_location field in UserProfile model
        user_profile.current_location = address
        user_profile.save()

    return render(request, 'map/map_call.html')


from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Station, TaxiCallNotification
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
# Create your views here.


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
    else:
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

# @login_required
# def map_call(request):
#     if request.method == 'POST':
#         address = request.POST.get('address')
#         user_profile = request.user.userprofile
#
#         # Update the user's current_location field in UserProfile model
#         user_profile.current_location = address
#         user_profile.save()
#     return render(request, 'map/map_call.html')


@login_required
def map_call(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        user_profile = request.user.userprofile

        # Update the user's current_location field in UserProfile model
        user_profile.current_location = address
        user_profile = TaxiCallNotification()
        user_profile.save()
        #
        print("POST 입니다.")
        print(user_profile)
    return render(request, 'map/map_call.html')



class TaxiCallListView(View):
    template_name = 'map/notifications_list.html'  # 템플릿 파일의 경로

    def get(self, request, *args, **kwargs):
        notifications = TaxiCallNotification.objects.all()
        print(notifications)
        context = {'notifications': notifications}
        return render(request, self.template_name, context)

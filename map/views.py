from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
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
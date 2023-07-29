from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def custom_logout(request):
    logout(request)
    return redirect('map/map_main')
@login_required
def my_page(request):
    user = request.user
    # 사용자에게 보여줄 마이페이지 정보를 준비합니다.
    context = {
        'user': user,
        # 여기에 추가적인 데이터를 준비하여 마이페이지에 사용할 수 있습니다.
    }
    return render(request, 'profiles/mypage.html', context)
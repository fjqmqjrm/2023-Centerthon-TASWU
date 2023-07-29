from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TaxiDriverForm
# Create your views here.

def custom_logout(request):
    logout(request)
    return redirect('map:map_main')

@login_required
def my_page(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = TaxiDriverForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('map:map_main')  # 폼 저장 후 프로필 페이지로 리디렉션
    else:
        form = TaxiDriverForm(instance=user_profile)

    context = {
        'user': request.user,
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profiles/mypage.html', context)


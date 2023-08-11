from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import TaxiDriverForm, phoneNumberForm
from .models import UserProfile, Station
from django.http import JsonResponse
# Create your views here.
def start_login(request):
    return render(request, 'profiles/mainlogin.html')

def custom_logout(request):
    logout(request)
    return redirect('map:map_main')

@login_required
def my_page(request):
    user_profile = UserProfile.objects.get(user=request.user)
    stations = Station.objects.all()

    if request.method == 'POST':
        form = TaxiDriverForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('map:map_main')  # 폼 저장 후 프로필 페이지로 리디렉션
    else:
        form = TaxiDriverForm(instance=user_profile)
        
    phone_number = user_profile.phone_number
        
    context = {
        'user': request.user,
        'user_profile': user_profile,
        'form': form,
        'phone_number': phone_number,
        'stations': stations,
    }
    return render(request, 'profiles/mypage.html', context)

@login_required
def call_list(request):
    return render(request, 'profiles/call_list.html')

@login_required
def update_profile_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.image = request.FILES['image']
        user_profile.save()

        return JsonResponse({'success': True, 'image_url': user_profile.image.url})
    return JsonResponse({'success': False})

@login_required
def phone_number(request):   
    user_profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = phoneNumberForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profiles:my_page')
    else:
        form = phoneNumberForm(instance=user_profile)
    return render(request, 'profiles/phone_number.html')


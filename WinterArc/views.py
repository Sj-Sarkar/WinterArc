# from django.shortcuts import render, redirect
# from .models import PlayerRegistration, PlayerStats, PendingRegistration
# from .decorators import superuser_required
# from django.shortcuts import render,HttpResponse


# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PendingRegistration


# Create your views here.
def home(request):
    return render(request,'home.html')
def head(request):
    return render(request,'header.html')
def foot(request):
    return render(request,'footer.html')
def scorecard(request):
    return render(request,'scorecard.html')
# def registration(request):
#     return render(request,'registration.html')
def contact(request):
    return render(request,'contact.html')


# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PendingRegistration

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_photo = request.FILES.get('profile_photo')
        confirm = request.POST.get('confirm')

        if confirm:
            en = PendingRegistration(
                name=name,
                dob=dob,
                phone=phone,
                email=email,
                profile_photo=profile_photo,
                approved=False
            )
            en.save()
            return render(request, 'registrationdone.html')
    return render(request, 'register.html')

# views.py
from django.shortcuts import render
from .models import PlayerStats, PlayerRegistration

def player_stats(request):
    players = PlayerStats.objects.select_related('player').all()
    return render(request, 'player_stats.html', {'players': players})

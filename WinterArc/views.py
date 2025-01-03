# from django.shortcuts import render, redirect
# from .models import PlayerRegistration, PlayerStats, PendingRegistration
# from .decorators import superuser_required
# from django.shortcuts import render, HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import PendingRegistration, PlayerRegistration, PlayerStats, Match, Scorecard
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def home(request):
    return render(request, 'home.html')

def head(request):
    return render(request, 'header.html')

def foot(request):
    return render(request, 'footer.html')

def scorecard(request):
    return render(request, 'scorecard.html')

def contact(request):
    return render(request, 'contact.html')

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

def player_stats(request):
    players = PlayerStats.objects.select_related('player').all()
    return render(request, 'player_stats.html', {'players': players})

def is_admin(user):
    return user.is_superuser

#@user_passes_test(is_admin, login_url='/login/')
# def create_scorecard_view(request):
#     if request.method == 'POST':
#         player_id = request.POST.get('player_id')  # Fetch the hidden input field for player ID
#         match_id = request.POST.get('match')
#         print(f"Player ID: {player_id}, Match ID: {match_id}")  # Debugging statement
#         player = get_object_or_404(PlayerRegistration, pk=player_id)
#         match = get_object_or_404(Match, pk=match_id)
        
#         scorecard = Scorecard(
#             match=match,
#             player=player,
#             innings=request.POST.get('innings'),
#             runs=request.POST.get('runs'),
#             balls=request.POST.get('balls'),
#             how_out=request.POST.get('how_out'),
#             overs=request.POST.get('overs'),
#             wickets=request.POST.get('wickets'),
#             runs_conceded=request.POST.get('runs_conceded'),
#             submitted=True
#         )
#         scorecard.save()
#         return render(request, 'scorecard_success.html')
    
#     players = PlayerRegistration.objects.all()
#     matches = Match.objects.all()
#     return render(request, 'create_scorecard.html', {'players': players, 'matches': matches})

from django.shortcuts import render
from .models import Match, Scorecard

def match_selection_view(request):
    matches = Match.objects.all()
    context = {
        'matches': matches
    }
    return render(request, 'match_selection.html', context)

def scorecard_view(request):
    match_number = request.GET.get('match_number')
    matches = Match.objects.all()
    selected_match = None
    innings_list = []

    if match_number:
        selected_match = Match.objects.get(match_number=match_number)
        scorecards = Scorecard.objects.filter(match=selected_match)
        
        for innings in ['1st', '2nd']:
            batsmen = scorecards.filter(innings=innings).exclude(runs__isnull=True, balls__isnull=True, strike_rate__isnull=True, how_out__isnull=True)
            bowlers = scorecards.filter(innings=innings).exclude(overs__isnull=True, wickets__isnull=True, economy__isnull=True, runs_conceded__isnull=True)
            
            innings_data = {
                'innings': innings,
                'batsmen': batsmen,
                'bowlers': bowlers,
                'total_runs': sum(score.runs for score in batsmen if score.runs is not None),
                'total_wickets': batsmen.count()
            }
            innings_list.append(innings_data)

    context = {
        'matches': matches,
        'selected_match': selected_match,
        'innings_list': innings_list
    }
    return render(request, 'scorecard.html', context)



from django.shortcuts import render, get_object_or_404
from WinterArc.models import Match, Scorecard

def home(request):
    matches = Match.objects.all()
    context = {
        'matches': matches
    }
    return render(request, 'home.html', context)

def match_selection_home(request):
    matches = Match.objects.all()
    context = {
        'matches': matches
    }
    return render(request, 'match_selection_home.html', context)


from django.shortcuts import render, get_object_or_404
from WinterArc.models import Match, Scorecard

def homecontents(request):
    match_number = request.GET.get('match_number')
    selected_match = None
    innings_list = []

    if match_number:
        selected_match = get_object_or_404(Match, match_number=match_number)
        scorecards = Scorecard.objects.filter(match=selected_match)

        for innings in ['1st', '2nd']:
            batsmen = list(scorecards.filter(innings=innings).exclude(runs__isnull=True, balls__isnull=True).order_by('-runs', 'balls')[:4])
            bowlers = list(scorecards.filter(innings=innings).exclude(wickets__isnull=True, runs_conceded__isnull=True).order_by('-wickets', 'runs_conceded')[:4])

            # Ensure both lists have the same length by padding with None
            max_length = max(len(batsmen), len(bowlers))
            batsmen.extend([None] * (max_length - len(batsmen)))
            bowlers.extend([None] * (max_length - len(bowlers)))

            innings_data = list(zip(batsmen, bowlers))
            innings_list.append(innings_data)

    context = {
        'selected_match': selected_match,
        'innings_list': innings_list
    }
    return render(request, 'homecontents.html', context)

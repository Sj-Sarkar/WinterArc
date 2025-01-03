# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Scorecard, PlayerStats

@receiver(post_save, sender=Scorecard)
def update_player_stats(sender, instance, **kwargs):
    player_stats, created = PlayerStats.objects.get_or_create(player=instance.player)
    
    # Ensure the values are integers or floats before performing the addition
    runs = int(instance.runs) if instance.runs else 0
    balls = int(instance.balls) if instance.balls else 0
    overs = float(instance.overs) if instance.overs else 0.0
    wickets = int(instance.wickets) if instance.wickets else 0
    runs_conceded = int(instance.runs_conceded) if instance.runs_conceded else 0

    # Check if the player has already been counted for this match
    if not Scorecard.objects.filter(player=instance.player, match=instance.match).exclude(id=instance.id).exists():
        player_stats.matches_played += 1

    player_stats.runs += runs
    player_stats.wickets += wickets
    player_stats.overs += overs
    player_stats.runs_conceded += runs_conceded

    # Calculate the economy rate
    player_stats.economy = player_stats.runs_conceded / player_stats.overs if player_stats.overs > 0 else 0.0

    player_stats.save()

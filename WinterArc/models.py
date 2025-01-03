# models.py
from django.db import models

class PendingRegistration(models.Model):
    phone = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Match(models.Model):
    match_number = models.IntegerField(unique=True)
    venue = models.CharField(max_length=100, default='Kalpataru Club Playground')

    def __str__(self):
        return f"Match {self.match_number}"

class PlayerRegistration(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    email = models.EmailField(unique=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PlayerStats(models.Model):
    player = models.OneToOneField(PlayerRegistration, on_delete=models.CASCADE)
    matches_played = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    average = models.FloatField(null=True)
    economy = models.FloatField(null=True)
    overs = models.FloatField(default=0.0)
    runs_conceded = models.IntegerField(default=0)

    def __str__(self):
        return f"Stats for {self.player.name}"
    
    def save(self, *args, **kwargs):
        if self.runs is not None and self.matches_played is not None and int(self.matches_played) > 0:
            self.average = (self.runs / self.matches_played)
        else:
            self.average = None

        if self.overs is not None and self.runs_conceded is not None and float(self.overs) > 0:
            self.economy = float(self.runs_conceded) / float(self.overs)
        else:
            self.economy = None

        super().save(*args, **kwargs)

class Scorecard(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(PlayerRegistration, on_delete=models.CASCADE)
    innings = models.CharField(max_length=10, choices=[('1st', '1st Innings'), ('2nd', '2nd Innings')])
    runs = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    strike_rate = models.FloatField(blank=True, null=True)
    how_out = models.CharField(max_length=100, blank=True, null=True)
    overs = models.FloatField(blank=True, null=True)
    wickets = models.IntegerField(blank=True, null=True)
    economy = models.FloatField(blank=True, null=True)
    runs_conceded = models.IntegerField(blank=True, null=True)
    submitted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player.name} - Match {self.match.match_number} - {self.innings}"

    def save(self, *args, **kwargs):
        if self.runs is not None and self.balls is not None and int(self.balls) > 0:
            self.strike_rate = (int(self.runs) / int(self.balls)) * 100
        else:
            self.strike_rate = None

        if self.overs is not None and self.runs_conceded is not None and float(self.overs) > 0:
            self.economy = float(self.runs_conceded) / float(self.overs)
        else:
            self.economy = None

        super().save(*args, **kwargs)

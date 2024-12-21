# models.py
from email.policy import default
from django.db import models


class PendingRegistration(models.Model):
    phone = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    


class PlayerRegistration(models.Model):
    phone = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PlayerStats(models.Model):
    player = models.OneToOneField(PlayerRegistration, on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    economy = models.FloatField(default=0.0)

    def __str__(self):
        return f"Stats for {self.player.name}"




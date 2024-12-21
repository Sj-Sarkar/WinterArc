
# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import PlayerRegistration, PlayerStats, PendingRegistration

@admin.register(PlayerRegistration)
class PlayerRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'dob', 'profile_photo_preview', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'phone', 'email')

    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_photo.url)
        return ""
    profile_photo_preview.short_description = 'Profile Photo'

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ('player', 'runs', 'wickets', 'average', 'economy')
    search_fields = ('player__name', 'player__phone', 'player__email')

def approve_registrations(modeladmin, request, queryset):
    for registration in queryset:
        PlayerRegistration.objects.create(
            name=registration.name,
            dob=registration.dob,
            phone=registration.phone,
            email=registration.email,
            profile_photo=registration.profile_photo,
            approved=True
        )
        PlayerStats.objects.create(player=PlayerRegistration.objects.get(phone=registration.phone))
        registration.delete()

approve_registrations.short_description = "Approve selected registrations"

@admin.register(PendingRegistration)
class PendingRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'dob', 'profile_photo_preview', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'phone', 'email')
    actions = [approve_registrations]

    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_photo.url)
        return ""
    profile_photo_preview.short_description = 'Profile Photo'

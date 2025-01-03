# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import PlayerRegistration, PlayerStats, PendingRegistration, Match, Scorecard

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
    list_display = ('player', 'matches_played', 'runs', 'wickets', 'average', 'economy','overs','runs_conceded')
    search_fields = ('player__name', 'player__phone', 'player__email')

@admin.register(PendingRegistration)
class PendingRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'dob', 'profile_photo_preview', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'phone', 'email')
    actions = ['approve_registrations']

    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_photo.url)
        return ""
    profile_photo_preview.short_description = 'Profile Photo'

    def approve_registrations(self, request, queryset):
        for registration in queryset:
            player = PlayerRegistration.objects.create(
                name=registration.name,
                dob=registration.dob,
                phone=registration.phone,
                email=registration.email,
                profile_photo=registration.profile_photo,
                approved=True
            )
            PlayerStats.objects.create(player=player)
            registration.delete()
    approve_registrations.short_description = "Approve selected registrations"

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_number', 'venue')


# admin.py
# admin.py
from django.contrib import admin
from .models import Scorecard

# Check if the model is already registered
if not admin.site.is_registered(Scorecard):
    class ScorecardAdmin(admin.ModelAdmin):
        list_display = ('match', 'player', 'innings', 'submitted')
        readonly_fields = ('submitted',)

        def has_change_permission(self, request, obj=None):
            if obj and obj.submitted and not request.user.is_superuser:
                return False
            return super().has_change_permission(request, obj)

    admin.site.register(Scorecard, ScorecardAdmin)


from django.contrib import admin
from WinterArc import views
from django.urls import path
from .views import match_selection_view, register, scorecard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('home/', views.home, name='home'),
    path('match-selection-home/', views.match_selection_home, name='match_selection_home'),
    path('homecontents/', views.homecontents, name='homecontents'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('player-stats/', views.player_stats, name='player_stats'),
    path('match-selection/', match_selection_view, name='match_selection_view'),
    path('scorecard/', scorecard_view, name='scorecard_view'),
]

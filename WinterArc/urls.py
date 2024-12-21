from django.contrib import admin
from WinterArc import views
from django.urls import path,include
from .views import register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home'),
    path('home/',views.home,name='Home'),
    # path('register/',views.registration,name='registration'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register, name='register'),
    path('player-stats/', views.player_stats, name='player_stats'),
    path('scorecard/',views.scorecard,name='scorecard')
    # path('', include('Championship.urls')),
]



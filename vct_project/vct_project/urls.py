from django.urls import path, include

urlpatterns = [
    path('tournaments/', include('tournaments.urls')),
    path('teams/', include('teams.urls')),
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls')),
]
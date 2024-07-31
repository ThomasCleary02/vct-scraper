from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    current_team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True)
    agents = models.JSONField(default=list)

class PlayerStatistics(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    maps_played = models.IntegerField(default=0)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    kd = models.FloatField(default=0)
    kad = models.FloatField(default=0)
    acs = models.FloatField(default=0)
    kpr = models.FloatField(default=0)
    adr = models.FloatField(default=0)
    kast = models.FloatField(default=0)
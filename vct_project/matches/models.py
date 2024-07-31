from django.db import models

class Match(models.Model):
    tournament = models.ForeignKey('tournaments.Tournament', on_delete=models.CASCADE)
    date = models.DateField()
    team1 = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey('teams.Team', on_delete=models.CASCADE, related_name='team2_matches')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()

class Map(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()

class PlayerPerformance(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField
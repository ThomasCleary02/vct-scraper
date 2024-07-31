from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50)
    tier = models.CharField(max_length=10)
    organizer = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2)
    location_city = models.CharField(max_length=100)
    location_country = models.CharField(max_length=100)
    participants = models.IntegerField()
    winner = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, related_name='tournaments_won')
    runner_up = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, related_name='tournaments_runner_up')
    icon = models.URLField()
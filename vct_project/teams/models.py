from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    logo_light = models.URLField()
    logo_dark = models.URLField()
    s_tier_wins = models.IntegerField(default=0)
    top_3_placements = models.IntegerField(default=0)
    top_6_placements = models.IntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

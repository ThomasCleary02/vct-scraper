from django.core.management.base import BaseCommand
from scraper.scraper import scrape_tournaments, scrape_teams, scrape_players

class Command(BaseCommand):
    help = 'Run all scrapers'

    def handle(self, *args, **options):
        tournaments_url = 'https://example.com/tournaments'
        teams_url = 'https://example.com/teams'
        players_url = 'https://example.com/players'
        
        scrape_tournaments(tournaments_url)
        scrape_teams(teams_url)
        scrape_players(players_url)
        self.stdout.write(self.style.SUCCESS('Successfully ran all scrapers'))
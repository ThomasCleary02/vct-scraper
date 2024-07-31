import requests
from bs4 import BeautifulSoup
from tournaments.models import Tournament
from teams.models import Team
from players.models import Player, PlayerStatistics

def scrape_tournaments(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tournaments = soup.find_all('div', class_='gridRow tournament-highlighted-bg')
    
    for tournament in tournaments:
        name = tournament.find('div', class_='Tournament').find('a').text
        short_name = name.split()[-1]
        tier = tournament.find('div', class_='Tier').text.strip()
        organizer = tournament.find('div', class_='Organizer').text.strip()
        date_str = tournament.find('div', class_='Date').text.strip()
        prize_str = tournament.find('div', class_='Prize').text.strip()
        location = tournament.find('div', class_='Location').text.strip()
        participants = int(tournament.find('div', class_='PlayerNumber').find('span').text)
        
        # Parse date and prize
        start_date, end_date = parse_date(date_str)
        prize_pool = parse_prize(prize_str)
        
        # Parse location
        country, city = parse_location(location)
        
        # Get winner and runner-up
        winner = tournament.find('div', class_='Placement FirstPlace').find('a').text
        runner_up = tournament.find('div', class_='Placement SecondPlace').find('a').text
        
        # Get icon URL
        icon_url = tournament.find('img', class_='league-icon-small-image')['src']
        
        # Create Tournament object
        Tournament.objects.create(
            name=name,
            short_name=short_name,
            tier=tier,
            organizer=organizer,
            start_date=start_date,
            end_date=end_date,
            prize_pool=prize_pool,
            location_city=city,
            location_country=country,
            participants=participants,
            winner=Team.objects.get(name=winner),
            runner_up=Team.objects.get(name=runner_up),
            icon=icon_url
        )

def scrape_teams(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    teams = soup.find_all('tr', style='line-height:25px;text-align:center')
    
    for team in teams:
        name = team.find('span', class_='name').find('a').text
        logo_light = team.find('span', class_='team-template-lightmode').find('img')['src']
        logo_dark = team.find('span', class_='team-template-darkmode').find('img')['src']
        s_tier_wins = int(team.find_all('td')[3].text)
        top_3_placements = int(team.find_all('td')[4].text)
        top_6_placements = int(team.find_all('td')[5].text)
        total_earnings = parse_earnings(team.find_all('td')[6].text)
        
        Team.objects.create(
            name=name,
            short_name=name[:20],  # Adjust as needed
            logo_light=logo_light,
            logo_dark=logo_dark,
            s_tier_wins=s_tier_wins,
            top_3_placements=top_3_placements,
            top_6_placements=top_6_placements,
            total_earnings=total_earnings
        )

def scrape_players(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    players = soup.find_all('tr')
    
    for player in players[1:]:  # Skip header row
        cells = player.find_all('td')
        name = cells[1].find('a').text
        country = cells[1].find('img')['alt'] if cells[1].find('img')['alt'] != "" else None
        agents = [img['alt'] for img in cells[3].find_all('img')]
        
        player_obj = Player.objects.create(
            name=name,
            country=country,
            agents=agents
        )
        
        PlayerStatistics.objects.create(
            player=player_obj,
            maps_played=int(cells[4].text),
            kills=int(cells[5].text),
            deaths=int(cells[6].text),
            assists=int(cells[7].text),
            kd=float(cells[8].text),
            kad=float(cells[9].text),
            acs=float(cells[10].text),
            kpr=float(cells[11].text),
            adr=float(cells[12].text),
            kast=float(cells[13].text)
        )

# Helper functions
def parse_date(date_str):
    # Implement date parsing logic
    pass

def parse_prize(prize_str):
    # Implement prize parsing logic
    pass

def parse_location(location_str):
    # Implement location parsing logic
    pass

def parse_earnings(earnings_str):
    # Implement earnings parsing logic
    pass
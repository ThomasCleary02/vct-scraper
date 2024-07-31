import requests
from bs4 import BeautifulSoup

def get_valorant_s_tier_tournaments():
    url = "https://liquipedia.net/valorant/S-Tier_Tournaments"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tournament rows
    tournament_rows = soup.find_all('div', class_='gridRow tournament-highlighted-bg')
    
    tournaments = []
    
    for row in tournament_rows:
        tournament = {}
        
        # Extract tournament name
        tournament_header = row.find('div', class_='gridCell Tournament Header')
        if tournament_header:
            tournament['name'] = tournament_header.find('a').text.strip()
        
        # Extract date
        date_cell = row.find('div', class_='gridCell EventDetails Date Header')
        if date_cell:
            tournament['date'] = date_cell.text.strip()
        
        # Extract prize (if available)
        prize_cell = row.find('div', class_='gridCell EventDetails Prize Header')
        if prize_cell and not 'Blank' in prize_cell.get('class', []):
            tournament['prize'] = prize_cell.text.strip()
        else:
            tournament['prize'] = 'Not specified'
        
        # Extract location
        location_cell = row.find('div', class_='gridCell EventDetails Location Header')
        if location_cell:
            tournament['location'] = location_cell.text.strip()
        
        # Extract number of participants
        participants_cell = row.find('div', class_='gridCell EventDetails PlayerNumber Header')
        if participants_cell:
            tournament['participants'] = participants_cell.text.strip()
        
        # Extract first place
        first_place_cell = row.find('div', class_='gridCell Placement FirstPlace')
        if first_place_cell:
            tournament['first_place'] = first_place_cell.find('span', class_='name').text.strip()
        
        # Extract second place
        second_place_cell = row.find('div', class_='gridCell Placement SecondPlace')
        if second_place_cell:
            tournament['second_place'] = second_place_cell.find('span', class_='name').text.strip()
        
        tournaments.append(tournament)
    
    return tournaments

# Run the function and print the results
results = get_valorant_s_tier_tournaments()
for result in results:
    print(f"Tournament: {result.get('name', 'N/A')}")
    print(f"Date: {result.get('date', 'N/A')}")
    print(f"Prize: {result.get('prize', 'N/A')}")
    print(f"Location: {result.get('location', 'N/A')}")
    print(f"Participants: {result.get('participants', 'N/A')}")
    print(f"Winner: {result.get('first_place', 'N/A')}")
    print(f"Runner-up: {result.get('second_place', 'N/A')}")
    print()
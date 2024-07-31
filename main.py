import requests
from bs4 import BeautifulSoup

def get_valorant_champions_winners():
    url = "https://liquipedia.net/valorant/VALORANT_Champions_Tour/2021"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tournament card elements
    tournament_cards = soup.find_all('div', class_='divRow tournament-card-premier')
    
    winners = []
    
    for card in tournament_cards:
        tournament_name = card.find('div', class_='divCell Tournament Header').text.strip()
        
        first_place = card.find('div', class_='divCell Placement FirstPlace')
        second_place = card.find('div', class_='divCell Placement SecondPlace')
        
        if first_place and second_place:
            first_place_team = first_place.find('span', class_='team-template-text').text.strip()
            second_place_team = second_place.find('span', class_='team-template-text').text.strip()
            
            winners.append({
                'tournament': tournament_name,
                'first_place': first_place_team,
                'second_place': second_place_team
            })
    
    return winners

# Run the function and print the results
results = get_valorant_champions_winners()
for result in results:
    print(f"Tournament: {result['tournament']}")
    print(f"Winner: {result['first_place']}")
    print(f"Runner-up: {result['second_place']}")
    print()
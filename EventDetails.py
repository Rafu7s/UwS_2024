import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_events(event_ids):
    events = []
    for event_id in event_ids:
        url = f"https://rekrutacja.teamwsuws.pl/events/{event_id}"
        headers = {"api-key": f"{API_KEY}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            events.append(response.json())
        except requests.exceptions.RequestException as e:
            print(f'Error fetching events for ID {event_id}: {e}')
    return events

def save_and_print_events(event_ids):
    events = fetch_events(event_ids)
    with open('eventsdetails.json', 'w', encoding='utf-8') as file:
        json.dump(events, file, ensure_ascii=False, indent=4)
    print("Dane zostały zapisane do pliku eventsdetails.json")
    for event in events:
        print(event)

event_ids = [3, 4, 5, 6, 7, 8, 9]
save_and_print_events(event_ids)

import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")

def fetch_events():
    url = "https://rekrutacja.teamwsuws.pl/events/"
    headers = {"api-key": f"{API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        if data:
            with open('events.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("Dane zostały zapisane do pliku events.json")
            for event in data:
                print(event)
        else:
            print("API response is empty.")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych: {e}")

if __name__ == "__main__":
    fetch_events()
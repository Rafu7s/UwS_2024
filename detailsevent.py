import requests

def fetch_events():
    url = "https://rekrutacja.teamwsuws.pl/events/8"
    headers = {"api-key": "967927582e7ee59cb4a7d73a83cd827b"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        if data:
            for event in data:
                print(event)
        else:
            print("API response is empty.")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych: {e}")

if __name__ == "__main__":
    fetch_events()
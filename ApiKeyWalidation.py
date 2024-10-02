from dotenv import load_dotenv
import os

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz klucz API
api_key = os.getenv("API_KEY")

print(api_key)  # Sprawdź, czy klucz API został poprawnie załadowany

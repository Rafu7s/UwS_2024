import json
from flask import Flask, render_template
import requests
from flask import Flask, jsonify
import datetime
from dotenv import load_dotenv
import os

API_URL = "https://rekrutacja.teamwsuws.pl/events"
load_dotenv()
API_KEY = os.getenv("API_KEY")


app = Flask(__name__)

def fetch_events():
    url = 'https://rekrutacja.teamwsuws.pl/events'
    headers = {"api-key": f"{API_KEY}"
  }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def format_events(data):
    events = []
    for event in data:
        events.append({
            'title': event['name'],
            'start': event['start_time'],
        })
    return events
    #return json.dumps(events)

def get_event_details(event_id, api_key):

  url = f"https://rekrutacja.teamwsuws.pl/events/8"
  headers = {
    "api-key": f"{API_KEY}"
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    return response.json()
  else:
    print(f"Błąd przy pobieraniu danych: {response.text}")
    return None

event_id = 8
api_key = f"{API_KEY}"
event_data = get_event_details(event_id, api_key)
if event_data:
  print(event_data)

@app.route('/')
def index():

    events_data = fetch_events()
    formatted_events = format_events(events_data)
    return render_template('calendar.html', events=formatted_events)

@app.route('/get_events')
def get_events():
    events2 = [
        {'title': 'Wydarzenie 1', 'start': '2023-11-01'},
        {'title': 'Wydarzenie 2', 'start': '2023-11-05'}
    ]
    return jsonify(events2)

if __name__ == '__main__':
    app.run(debug=True)


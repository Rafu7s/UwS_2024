# Description
Calendar app to develop (first version)
<br>

# Used:
-pycharm 2024.1 <br>
-Git <br>
-API from UWS (Uniweristy from Siedlce) <br>
-modules: pip, request, flask, dotenv <br>
-Chrome

# Setup
1. run app.py file
2. open: http://127.0.0.1:5000
3. enjoy :)

   *active api key required to receive events via API, but the data can be taken from file 'events.json' or 'eventsdetails.json' for more details.
 <br>
 
### Done
-Widok miesięczny kalendarza: Przeglądaj wydarzenia zaplanowane na dany miesiąc.
![podgląd](images/2024-09-29_18h29_30.png)
 
### Todo
-Szczegóły wydarzenia: Po kliknięciu na konkretne wydarzenie, użytkownik powinien móc zobaczyć jego szczegółowe informacje.

<br>

#### Notes <br>
ApiKeyWalidation.py - checking connection with API  <br>
EventDetails.py & EventsListDownload.py - to download and save the data from API locally

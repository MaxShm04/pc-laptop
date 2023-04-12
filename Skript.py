import calendar
import lib
import math
import os
import pickle
from datetime import datetime

from google.protobuf import service
from google_auth_httplib2 import Request

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL

# client_secret_537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta
import pytz
import requests


def main():
    token_path = "D:\\Prog\\googleApi\\token.json"
    calendar_Id = "b6e298b82352d3cceadbf543a39c5147bcada63f74a6c9fd013d5769e0ae7507@group.calendar.google.com"
    client_secret = 'D:\Prog\googleApi\client_secret_537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com.json'
    client_id = "537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com"
    client_secret_id = "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"
    refresh_token_url = 'https://accounts.google.com/o/oauth2/token'

    # Scopes definieren, z.B. für den Google-Kalender
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Credentials-Datei (JSON) einlesen
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # Wenn noch keine Credentials existieren oder diese abgelaufen sind, den Autorisierungs-Flow starten
    if not creds or not creds.valid:
        if creds is not None and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret,SCOPES)  # Ersetzen Sie 'client_secret.json' durch den Pfad zu Ihrer Client-ID und Ihrem Client-Secret
            creds = flow.run_local_server(port=0)
            creds = flow.run_local_server(access_type='offline')
            # Speichern Sie die Credentials für die zukünftige Verwendung
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        creds = Credentials.from_authorized_user_info('token.pickle', SCOPES)  # 'info' enthält die Zugriffsdaten, die Sie in Schritt 1 erhalten haben

        params = {
            'client_id': client_id,
            'client_secret': client_secret_id,
            'grant_type': 'refresh_token',
            'refresh_token': creds.refresh_token
        }
        response = requests.post(refresh_token_url, data=params)
        response_data = response.json()

        if 'refresh_token' in response_data:
            print('Refresh Token erfolgreich abgerufen:')
            print(response_data['refresh_token'])
        else:
            print('Fehler beim Abrufen des Refresh Tokens:')
            print(response_data['error'])

        # Neue Credentials in JSON-Datei speichern
        with open('D:\\Prog\\googleApi\\token.json', 'w') as token:
            token.write(creds.to_json())

        refresh_token = response_data['refresh_token']  # Das neue Refresh Token
    ''' calendar = service.calendars().get(calendarId='537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com').execute()
    print(calendar['summary'])'''

    response = requests.get('https://www.googleapis.com/calendar/v3/calendars/calendarId/events')
    if response.status_code == 200:
        print('Anfrage erfolgreich.')
        print(response.json())
    else:
        print('Fehler beim Abrufen der Daten. Status Code:', response.status_code)

    call_calendar(token_path, calendar_Id)

    return


def call_calendar(token, calendar_Id):
    # Set timezone to your local timezone
    local_timezone = pytz.timezone('Europe/Berlin')

    # Authenticate and build the service
    creds = Credentials.from_authorized_user_file(token, ['https://www.googleapis.com/auth/calendar'])
    service = build('calendar', 'v3', credentials=creds)

    # Define start and end time
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    end_time = datetime.utcnow() + timedelta(days=1)
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)
    end_time = end_time.isoformat() + 'Z'

    # Call the Calendar API
    try:
        events_result = service.events().list(calendarId=calendar_Id, timeMin=now, timeMax=end_time, maxResults=1,
                                              singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
        else:
            print(len(events))
            for n in range(len(events)):
                event = events[n - 1]
                start_time = event['start'].get('dateTime', event['start'].get('date'))
                end_time2 = event['end'].get('dateTime', event['end'].get('date'))
                start_time = datetime.fromisoformat(start_time).replace(tzinfo=pytz.UTC)
                start_time_local = start_time.astimezone(local_timezone)
                end_time2 = datetime.fromisoformat(end_time2).replace(tzinfo=pytz.UTC)
                end_time2_local = start_time.astimezone(local_timezone)
                print(f'Start Time (Local Timezone): {start_time_local}')
                print(f'Summary: {event["summary"]}')
                # print(f'Location: {event["location"]}')
                if start_time < datetime.now(pytz.UTC):
                    print('This event has already started.')
                    if end_time2 < datetime.now(pytz.UTC):
                        print('This event has already ended.')
                    else:
                        open_files(event["summary"])
                        print('This event has not ended yet.')
                else:
                    print('This event has not started yet.')

                print("-" * 30)
    except HttpError as error:
        print(f'An error occurred: {error}')


def open_files(summary):
    # file paths:
    paths = {
        "sem_path": r"D:\Uni\Sem 2",
        "Betriebssysteme": r"D:\Uni\Sem 2\Betriebssysteme\Skript-IT-Grundlagen-WI22-Vorlesung-Teil-2.pdf",
        "Engineering": r"D:\Uni\Sem 2\Finanzdienstleistung\Bedke_Altersvorsorge.pdf",
        "Recht": r"D:\Uni\Sem 2\Handels- und Gesellschaftsrecht\Kaufrecht 2023 - Handout.pdf",
        "Leistungsrechnung": r"D:\Uni\Sem 2\Kosten- und Leistungsrechnung\Skript WI_Kosten- und Leistungsrechnung_Laub.pdf",
        "Logik": r"D:\Uni\Sem 2\Logik und Algebra\Logik und Algebra.pdf",
        "Präsentationstechnik": r"D:\Uni\Sem 2\Präsentationstechnik\Geyer_Skript 2023 WI.pdf",
        "Programmierung": r"D:\Uni\Sem 2\Programmieren\01_Intro.pdf",
        "Systemanalyse": r"D:\Uni\Sem 2\Systemanalyse und -entwurf\Avila de Block_Skript DHBW-VS, 2023, Systemanalyse -entwurf.pdf"
    }
    for x in paths.values():
        if os.path.exists(x):
            print(x)
        else:
            print(ValueError)
            return
    for x in paths.keys():
        if x.lower() in summary.lower():
            os.startfile(paths.get(x))
            print("open")


if __name__ == '__main__':
    # time = datetime.now()
    main()
    #open_files("Fortgeschrittene Programmierung VS-WWI22C + W3WI_109.2 Algorithmen und Datenstrukturen")
# rint(datetime.now() - time)

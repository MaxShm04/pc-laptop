import calendar
import lib
import math
import os
from datetime import datetime

from google.protobuf import service

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL

#client_secret_537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta
import pytz

def main():

    token_path = "D:\\Prog\\googleApi\\token.json"
    calendar_Id = "b6e298b82352d3cceadbf543a39c5147bcada63f74a6c9fd013d5769e0ae7507@group.calendar.google.com"

    # Scopes definieren, z.B. für den Google-Kalender
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Credentials-Datei (JSON) einlesen
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # Wenn noch keine Credentials existieren oder diese abgelaufen sind, den Autorisierungs-Flow starten
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('D:\Prog\googleApi\client_secret_537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com.json', SCOPES)
        creds = flow.run_local_server(access_type='offline')
        creds = flow.run_local_server(port=0)

        # Neue Credentials in JSON-Datei speichern
        with open('D:\\Prog\\googleApi\\token.json', 'w') as token:
            token.write(creds.to_json())

    ''' calendar = service.calendars().get(calendarId='537588646904-fgbtn9saslu0q5on1rntq7179vau23mv.apps.googleusercontent.com').execute()
    print(calendar['summary'])'''

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
        events_result = service.events().list(calendarId=calendar_Id, timeMin=now, timeMax=end_time, maxResults=5,
                                              singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('No upcoming events found.')
        else:
            print(len(events))
            for n in range(len(events)):
                event = events[n-1]
                start_time = event['start'].get('dateTime', event['start'].get('date'))
                end_time2 = event['end'].get('dateTime', event['end'].get('date'))
                start_time = datetime.fromisoformat(start_time).replace(tzinfo=pytz.UTC)
                start_time_local = start_time.astimezone(local_timezone)
                end_time2 = datetime.fromisoformat(end_time2).replace(tzinfo=pytz.UTC)
                end_time2_local = start_time.astimezone(local_timezone)
                print(f'Start Time (Local Timezone): {start_time_local}')
                print(f'Summary: {event["summary"]}')
                #print(f'Location: {event["location"]}')
                if start_time < datetime.now(pytz.UTC):
                    print('This event has already started.')
                    if end_time2 < datetime.now(pytz.UTC):
                        print('This event has already ended.')
                    else:
                        print('This event has not ended yet.')
                else:
                    print('This event has not started yet.')

                print("-"*30)

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    time = datetime.now()
    main()
    print(datetime.now() - time)


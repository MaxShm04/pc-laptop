import http.client
import json
from data import client_id, client_secret, refresh_token, code
from urllib.parse import urlencode  # Importieren Sie urlencode
import boto3


def get_access_token_with_code(code, redirect_uri):
    conn = http.client.HTTPSConnection("www.strava.com")
    payload = urlencode({
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    })
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read().decode()
    if res.status == 200:
        return json.loads(data)['access_token'], json.loads(data)['refresh_token']
    else:
        print("Fehler beim Abrufen des Zugriffstokens:", data)
        return None, None


def get_activities(access_token):
    activities_url = "/api/v3/athlete/activities"
    conn = http.client.HTTPSConnection("www.strava.com")
    headers = {'Authorization': 'Bearer ' + access_token}

    request_page_num = 1
    all_activities = []

    while True:
        # Korrektur: Stellen Sie sicher, dass die Parameter korrekt als Query-String formatiert sind
        params = f'per_page=20&page={request_page_num}'  # Direkte String-Formatierung
        conn.request("GET", activities_url + "?" + params, headers=headers)  # Korrigierte Anfrage
        res = conn.getresponse()
        my_dataset = json.loads(res.read().decode("utf-8"))

        if 'message' in my_dataset and my_dataset['message'] == 'Rate Limit Exceeded':
            print(all_activities)
            print(my_dataset)
            print("Rate Limit Exceeded - breaking out of the loop.")
            break

        if 'message' in my_dataset and my_dataset['message'] == 'Authorization Error':
            print(all_activities)
            print(my_dataset)
            print("Authorization Error - breaking out of the loop.")
            break

        if not my_dataset:  # Eine leere Liste prüfen
            print(
                "breaking out of while loop because the response is zero, which means there must be no more activities")
            break

        # my_dataset ist eine Liste, daher verwenden wir extend, um all_activities zu erweitern
        print("Extending all_activities with the new dataset")
        print(my_dataset)
        all_activities.extend(my_dataset)  # Funktioniert, da my_dataset eine Liste ist

        request_page_num += 1

    return all_activities


def write_activities_to_s3(bucket_name, activities_data):
    s3 = boto3.client('s3')
    filename = 'activities.json'  # Oder generieren Sie einen dynamischen Dateinamen
    s3.put_object(Bucket=bucket_name, Key=filename, Body=json.dumps(activities_data))


def lambda_handler(event, context):
    redirect_uri = "https://eu-north-1.console.aws.amazon.com/lambda/home?region=eu-north-1#/functions/stravaActivities?tab=code"

    print("Requesting Token...\n")
    access_token, refresh_token = get_access_token_with_code(code, redirect_uri)
    if access_token:
        print("Access Token =", access_token)
        activities = get_activities(access_token)
        print(len(activities))
        for count, activity in enumerate(activities):
            print(activity["name"])
            print(count)

        print(activities)
        activities_json = '\n'.join(json.dumps(activity) for activity in activities)
        bucket_name = 'stravaapi'
        write_activities_to_s3(bucket_name, activities_json)
        print(f"Successfully uploaded activities to S3 bucket '{bucket_name}'")


    else:
        print("Kein Zugriffstoken erhalten.")


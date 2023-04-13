import lib
import math
from datetime import datetime, timedelta

import pytz

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL
import Skript

import multiprocessing
import time

global y

def stop():
    y = False
    return

def background_process():
    while True:
        print("Dies ist ein Hintergrundprozess")
        time.sleep(1)


if __name__ == '__main__':
    # Starten des Hintergrundprozesses
    #p = multiprocessing.Process(target=background_process)
    #p.start()
    y = True
    wait = datetime.now(pytz.UTC)
    mark = None
    local_timezone = pytz.timezone('Europe/Berlin')
    # Hauptprozess fortfahren
    while y == True:
        #print("Dies ist der Hauptprozess")
        if wait <= datetime.now(pytz.UTC) + timedelta(minutes=15):
            print(wait)
            print(datetime.now(pytz.UTC))
            token_path, calendar_id = Skript.start()
            x = Skript.call_calendar(token_path, calendar_id)
            if x[0] and x[1]:
                Skript.open_files(x)
            if x[0] and not x[1]:
                wait = x[1]
                print(wait)
                wait = wait.astimezone(local_timezone)
                print(wait)
        else:
            print("wait")
        print(f"Wait till {wait}")
        time.sleep(5)

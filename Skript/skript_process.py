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
            x = Skript.get_current_event(token_path, calendar_id)
            wait = Skript.get_next_event(token_path, calendar_id)[1]
        else:
            print("wait")
        print(f"Now:{datetime.now(pytz.UTC)} Wait till {wait}")
        time.sleep(5)

#last
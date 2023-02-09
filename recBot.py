import lib
import math
import time
from datetime import datetime

lib.sync(r'C:\Users\MrXam\PycharmProjects\duzzelLibrary\eulerLib.py')
import eulerLib as eL


import pyautogui
import keyboard
while True:
    res = pyautogui.locateOnScreen("gb.png")
    if res is not None:
        for n in range(1, 5):
            time.sleep(n)
        print(res)
        x, y = pyautogui.center(res)
        x1, y1 = pyautogui.position()
        pyautogui.leftClick(x,y)
        pyautogui.moveTo(x1, y1)
    if keyboard.is_pressed("n"):
        break

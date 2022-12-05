import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
mainRoot = ROOT_DIR[:int(ROOT_DIR.find("Python_Hausaufgaben"))]
#print("ROOTDIR " + ROOT_DIR)
mainRoot += "duzzelLibrary"
import sys
#print(mainRoot+"duzzelLibrary")
sys.path.append(os.path.abspath(mainRoot+"duzzelLibrary"))
SYS_ROOT_DIR = os.path.dirname(os.path.abspath(sys.executable))
SYS_ROOT_DIR += "\lib"
import shutil
shutil.copy(mainRoot+"\eulerLib.py", SYS_ROOT_DIR)
print("Sync successful")




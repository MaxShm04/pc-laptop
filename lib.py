import os
import sys
import shutil
def sync(file):
    '''
    write __file__ as argument

    :param file: __file__
    :return: nothing
    '''
    ROOT_DIR = os.path.dirname(os.path.abspath(file))
    mainRoot = ROOT_DIR[:int(ROOT_DIR.find("Python_Hausaufgaben"))]
    mainRoot += "duzzelLibrary"
    sys.path.append(os.path.abspath(mainRoot + "duzzelLibrary"))
    SYS_ROOT_DIR = os.path.dirname(os.path.abspath(sys.executable))
    SYS_ROOT_DIR += "\lib"
    shutil.copy(mainRoot + "\eulerLib.py", SYS_ROOT_DIR)
    #print("Sync successful")


import os
import sys
import shutil
def sync(libPath):
    '''
    write libPath as argument

    :param str: libPath
    :return: nothing
    '''
    #ROOT_DIR = os.path.dirname(os.path.abspath(file))       #file dir
    #mainRoot = ROOT_DIR[:int(ROOT_DIR.find("Python_Hausaufgaben"))]
    #mainRoot += "duzzelLibrary"
    #sys.path.append(os.path.abspath(libPath))
    SYS_ROOT_DIR = os.path.dirname(os.path.abspath(sys.executable))
    SYS_ROOT_DIR += "\lib"
    #print(libPath)
    #print(SYS_ROOT_DIR)
    shutil.copy(libPath, SYS_ROOT_DIR)
    #print("Sync successful")


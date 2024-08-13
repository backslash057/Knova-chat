import time
import os
import os.path
from enum import Enum

logpath = None
symbol = ""

class logtypes(Enum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    WARNING = "WARNING"



def init(path, sym=""):
    global logpath, symbol

    logpath = path
    symbol = sym

    if not os.path.exists(logpath): os.mkdir(logpath)


def write(content, logtype=logtypes.DEBUG):
    if not os.path.exists(logpath): os.mkdir(logpath)
    if not type(logtype) == logtypes: return

    current = time.strftime("%H:%M:%S")
    logfile = time.strftime("%Y-%m-%d")
    
    log = f"[{current}] [{logtype.value}] {content}"

    logfile = open(os.path.join(logpath, logfile+".log"), "a")

    logfile.write(log + "\n")
    print(log)
    logfile.close()



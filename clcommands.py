__author__ = 'Sebastian'
import sys
from gopigo import *

command = str(sys.argv)

if command == "fwd":
    for x in range(5):
        time.sleep(0.1)
        fwd()

elif command == "stop":
    for x in range(6):
        stop()
        disable_servo()
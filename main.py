__author__ = 'Sebastian'
from gopigo import *
import time

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######

    #key value dictionary for basic state of pigo
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175}

    def __init__(self):
        print "Boop Beep"

    #named after method stop() in GoPiGo lib
    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(0.1)
            print "ERROR 01: Can't stop"

    #named after method fwd() in GoPiGo lib
    def fwd(self):
        self.isMoving = True
        while fwd() != 1:
            time.sleep(0.1)
            print "ERROR 02: Can't move fwd"

    ######
    ###### COMPLEX METHODS
    ######

    ######
    ###### MAIN APP STARTS HERE
    ######

myPigo = Pigo()
myPigo.fwd()
time.sleep(2)
myPigo.stop()
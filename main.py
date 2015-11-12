__author__ = 'Sebastian'
from gopigo import *
import time

#global variables begin here
STOP_DISTANCE = 50
#global variables begin here

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######
    #key value dictionary for basic state of pigo
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'dist' : 100}

    def __init__(self):
        print "I am alive with the magic of friendship!"
        self.status['dist'] = us_dist(15)

    #named after method stop() in GoPiGo lib
    def stop(self):
        self.status['ismoving'] = False
        print "Stop"
        for x in range(5):
            time.sleep(0.1)
            stop()

    #named after method fwd() in GoPiGo lib
    def fwd(self):
        self.status['ismoving'] = True
        print "Fwd"
        for x in range(10):
            time.sleep(0.1)
            fwd()

    #used to tell the main loop to keep going unless something goes wrong
    def keepGoing(self):
        if self.status['dist'] < STOP_DISTANCE:
            print "WARNING 03: Too close to object"
            return False
        elif volt() > 14 or volt() < 6:
            print "WARNING 02: Voltage outside of safe range: " + str(volt())
            return False
        else:
            return True

    #used to check distance
    def checkDistance(self):
        self.status['dist'] = us_dist(15)
        print "dist = " + str(self.status['dist']) + " mm"

    ######
    ###### COMPLEX METHODS
    ######

    def dance(self):
        print "MONEY"
        self.spin()
        self.backNForth()
        self.strobe()
        self.servoShake()

    def spin(self):
        for x in range(5):
            time.sleep(0.1)
            set_speed(251)
            left_rot()

    def backNForth(self):
        for x in range(5)
            time.sleep(0.1)
            set_speed(251)
            fwd()
            time.sleep(2)
            bwd()
            time.sleep(2)

    def strobe(self):
	    print "let's have a rager!"
	    for x in range(7):
		    led_on(1)
		    led_off(0)
		    led_off(1)
		    led_on(0)

    def servoShake(self):
        for x in range(5):
            servo(45)
            servo(135)
######
###### MAIN APP STARTS HERE
######
pinkie = Pigo()

while pinkie.keepGoing():
    pinkie.checkDistance()
    pinkie.fwd()
    time.sleep(.1)
    pinkie.stop()
    pinkie.checkDistance()
    pinkie.dance()

pinkie.stop()
del pinkie
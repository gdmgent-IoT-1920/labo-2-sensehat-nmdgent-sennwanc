from sense_hat import SenseHat
import sys
import time
import random

sense = SenseHat()

def runThroughLeds():
    while True:
        for x in range(8):
            for y in range (8):
                r = random.randrange(0,255)
                g = random.randrange(0,255)
                b = random.randrange(0,255)
                sense.set_pixel(x,y,r,g,b)
                time.sleep(0.2)
                sense.clear()
try:
    runThroughLeds()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
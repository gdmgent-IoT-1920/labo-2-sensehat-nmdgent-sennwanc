from sense_hat import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    # feet
    sense.set_pixel(3,7,150,75,0)
    sense.set_pixel(4,7,150,75,0)
    # legs
    sense.set_pixel(3,6,0,0,255)
    sense.set_pixel(4,6,0,0,255)
    # body
    sense.set_pixel(3,5,255,0,0)
    sense.set_pixel(4,5,255,0,0)
    sense.set_pixel(3,4,255,0,0)
    sense.set_pixel(4,4,255,0,0)
    # arms
    sense.set_pixel(2,4,255,0,0)
    sense.set_pixel(5,4,255,0,0)
    sense.set_pixel(1,5,255,241,195)
    sense.set_pixel(6,5,255,241,195)
    # head
    sense.set_pixel(3,3,255,241,195)
    sense.set_pixel(4,3,255,241,195)
    sense.set_pixel(3,2,255,241,195)
    sense.set_pixel(4,2,255,241,195)
   
    while True:
        for x in sense.stick.get_events():
            if x.direction == 'up':
                sense.clear()
                y=1
                # feet
                sense.set_pixel(3,7-y,150,75,0)
                sense.set_pixel(4,7-y,150,75,0)
                # legs
                sense.set_pixel(3,6-y,0,0,255)
                sense.set_pixel(4,6-y,0,0,255)
                # body
                sense.set_pixel(3,5-y,255,0,0)
                sense.set_pixel(4,5-y,255,0,0)
                sense.set_pixel(3,4-y,255,0,0)
                sense.set_pixel(4,4-y,255,0,0)
                # arms
                sense.set_pixel(2,4-y,255,0,0)
                sense.set_pixel(5,4-y,255,0,0)
                sense.set_pixel(1,5-y,255,241,195)
                sense.set_pixel(6,5-y,255,241,195)
                # head
                sense.set_pixel(3,3-y,255,241,195)
                sense.set_pixel(4,3-y,255,241,195)
                sense.set_pixel(3,2-y,255,241,195)
                sense.set_pixel(4,2-y,255,241,195)
                time.sleep(1)
                sense.clear()
                main()
            elif x.direction == 'down':
                sense.clear()
            elif x.direction == 'left':
                sense.clear()
            elif x.direction == 'right':
                sense.clear()
            elif x.direction == 'middle':
                sense.clear()
    
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
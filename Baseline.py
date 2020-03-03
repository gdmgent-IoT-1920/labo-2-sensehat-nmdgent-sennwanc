from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    text = "Hello we are New Media Devolopment:)"
    while True:        
        r = random.randrange(0,255)
        g = random.randrange(0,255)
        b = random.randrange(0,255)
        
        rb = random.randrange(0,r)
        gb = random.randrange(0,g)
        bb = random.randrange(0,b)
        
        sense.show_message(text, 0.1, [r, g, b], [rb,gb,bb])
        time.sleep(1)       
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()


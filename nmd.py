from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    text = "NMD"
    while True:        
        for x in text:
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            
            sense.show_letter(x, [r, g, b], [0,0,0])
            time.sleep(1)
        time.sleep(3)        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()

from sense_hat import SenseHat
import sys
import time

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    while True:
        # LEDS AANSTUREN
        """
        sense.set_pixel(0,0,0,255,0)
        sense.set_pixel(1,1,0,255,0)
        sense.set_pixel(2,2,0,255,0)
        sense.set_pixel(3,3,0,255,0)
        sense.set_pixel(4,4,0,255,0)
        sense.set_pixel(5,5,0,255,0)
        sense.set_pixel(6,6,0,255,0)
        sense.set_pixel(7,7,0,255,0)
        """
        
        # TEKST UITLEZEN NAAR SENSE HAT
        # message, snelheid, letterkleur, achtergrondkleur
        # sense.show_message("Senjé West", 0.1, [0,255,0], [0, 0, 0])
        
        # LETTERS UITLEZEN NAAR SENSE HAT
        # aparte letters
        sense.show_letter("Y",[0,255,0], [0, 0, 0])
        time.sleep(1)
        sense.show_letter("M",[255,0,0], [0, 0, 0])
        time.sleep(1)
        sense.show_letter("C",[0,0,255], [0, 0, 0])
        time.sleep(1)
        sense.show_letter("A",[255,255,255], [0, 0, 0])
        time.sleep(3)
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
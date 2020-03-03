from sense_hat import SenseHat
import sys
import time

sense = SenseHat()

def stepOne():
    sense.clear()
    X = [255, 0, 0] 
    O = [0, 0, 0]

    step_one = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

    sense.set_pixels(step_one)
    time.sleep(2)    
        
def stepTwo():
    X = [0, 255, 0] 
    O = [0, 0, 0]  

    step_two = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

    sense.set_pixels(step_two)
    time.sleep(2)
    
def stepThree():
    X = [0, 0, 255] 
    O = [0, 0, 0]  

    step_three = [
    O, O, O, O, O, O, O, O,
    O, X, X, X, X, X, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, X, X, X, X, X, O,
    O, O, O, O, O, O, O, O
    ]

    sense.set_pixels(step_three)
    time.sleep(2)

def stepFour():
    sense.clear()
    X = [255, 255, 0] 
    O = [0, 0, 0]

    step_four = [
    X, X, X, X, X, X, X, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, X, X, X, X, X, X, X
    ]

    sense.set_pixels(step_four)
    time.sleep(2)
    
def runSteps():
    while True:
        stepOne()
        sense.clear()
        stepTwo()
        sense.clear()
        stepThree()
        sense.clear()
        stepFour()
        sense.clear()
        stepThree()
        sense.clear()
        stepTwo()
        sense.clear()
try:
    runSteps()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()
    
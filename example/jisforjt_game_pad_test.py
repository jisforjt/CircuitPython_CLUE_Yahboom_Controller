# CircuitPython CLUE Yahboom jisforjt_controller_test.py

from jisforjt_controller import gamepad
from adafruit_clue import clue
import time

clue_data = clue.simple_text_display(title="Yahboom Sensor Data!", title_scale=2)

while True:
    ######################################################
    #   Display Data
    ######################################################
    clue_data[0].text = "Joystick X: {:.2f}".format(gamepad.x)
    clue_data[1].text = "Joystick Y: {:.2f}".format(gamepad.y)
    clue_data[2].text = "Joystick Press: {}".format(gamepad.press)

    clue_data[4].text = "Button B1: {}".format(gamepad.b1)
    clue_data[5].text = "Button B2: {}".format(gamepad.b2)
    clue_data[6].text = "Button B3: {}".format(gamepad.b3)
    clue_data[7].text = "Button B4: {}".format(gamepad.b4)

    clue_data.show()

    ######################################################
    #   Buzzer
    ######################################################
    # Uncomment the code below to hear the game pad buzz on 
    # and off every half a second. This only works if you have
    # the physical game pad switch set to software mode.
    
    #gamepad.buzz(0.5)
    #time.sleep(0.5)
    

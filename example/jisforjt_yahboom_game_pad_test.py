# CircuitPython CLUE Yahboom Game Pad jisforjt_yahboom_game_pad_test.py
# Last Updated Aug. 10, 2021
# Author(s): James Tobin

from jisforjt_yahboom_game_pad import gamepad
from adafruit_clue import clue
import time

clue_data = clue.simple_text_display(title="Yahboom Sensor Data!", title_scale=2)

while True:
    ######################################################
    #   Display Data
    ######################################################
    clue_data[0].text = "Joystick X Voltage: {:.2f}".format(gamepad.x_voltage)
    clue_data[1].text = "Joystick Y Voltage: {:.2f}".format(gamepad.y_voltage)
    clue_data[2].text = "Joystick X: {:.2f}".format(gamepad.x)
    clue_data[3].text = "Joystick X: {:.2f}".format(gamepad.x)
    
    clue_data[5].text = "Joystick Press: {}".format(gamepad.press)
    clue_data[6].text = "Button B1: {}".format(gamepad.b1)
    clue_data[7].text = "Button B2: {}".format(gamepad.b2)
    clue_data[8].text = "Button B3: {}".format(gamepad.b3)
    clue_data[9].text = "Button B4: {}".format(gamepad.b4)

    clue_data.show()

    ######################################################
    #   Buzzer
    ######################################################
    # This only works if you have the physical game pad 
    # switch set to software mode.
    if gamepad.press == True:
        gamepad.buzz(0.5)
        time.sleep(0.5)

    
    
    

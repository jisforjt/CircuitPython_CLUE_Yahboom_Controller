# CircuitPython CLUE Yahboom jisforjt_controller_test.py

from jisforjt_controller import controller
from adafruit_clue import clue
import time

#clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(title="Yahboom Sensor Data!", title_scale=2)

while True:
    clue_data[0].text = "Joystick X: {:.2f}".format(controller.x)
    clue_data[1].text = "Joystick Y: {:.2f}".format(controller.y)
    clue_data[2].text = "Joystick Press: {}".format(controller.press)

    clue_data[4].text = "Button B1: {}".format(controller.b1)
    clue_data[5].text = "Button B2: {}".format(controller.b2)
    clue_data[6].text = "Button B3: {}".format(controller.b3)
    clue_data[7].text = "Button B4: {}".format(controller.b4)

    clue_data[9].text = "Buzzer Off: {}".format(controller.buzz)

    clue_data.show()

    #controller.playTone(0.5)
    #time.sleep(2)
    

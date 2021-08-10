# CircuitPython Clue Yahboom Game Pad jisforjt_yahboom_game_pad.py
# Last Updated Aug. 10, 2021
# Author(s): James Tobin

######################################################
#   MIT License
######################################################
'''
Copyright (c) 2020 James Tobin
Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:
The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
'''

######################################################
#   Cutebot Information
######################################################
'''
jisforjt_Game_Pad.py:
v1
    This is a higher-level library to allow Adafruit's CLUE and Yahboom's micro:bit 
    Game Pad to communicate while maintaining all the functionality of the CLUE, 
    except for touch features.
'''

######################################################
#   Pin Reference
######################################################
"""
Pins
    P0  -Digital    Game Pad - Buzzer and Rumbler
    P1  -Analog     Game Pad - Joystick: Y
    P2  -Analog     Game Pad - Joystick: X
    P5  -Digital    Clue - Button A
    P8  -Digital    Game Pad - Joystick: Press
    P11 -Digital    Clue - Button B
    P13 -Digital    Game Pad - Button B1
    P14 -Digital    Game Pad - Button B2
    P15 -Digital    Game Pad - Button B3
    P16 -Digital    Game Pad - Button B4
    P17 -Digital    Clue - LED
    P18 -Digital    Clue - Neopixel
    P43 -Digital    Clue - White LEDs
"""


######################################################
#   Import
######################################################
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn

class Game_Pad:

    def __init__(self):
        # Define sound and rumble
        self._buzzer_rumbler = DigitalInOut(board.P0)
        self._buzzer_rumbler.direction = Direction.OUTPUT
        self._buzzer_rumbler.value = True

        # Define joystick pins
        self._joystick_y = AnalogIn(board.P1)
        self._joystick_x = AnalogIn(board.P2)
        
        # Define buttons
        # Joystick press
        self._joystick_press = DigitalInOut(board.D8)
        self._joystick_press.direction = Direction.INPUT
        self._joystick_press.pull = Pull.UP
        # B1
        self._b1 = DigitalInOut(board.D13)
        self._b1.direction = Direction.INPUT
        self._b1.pull = Pull.UP
        # B2
        self._b2 = DigitalInOut(board.D14)
        self._b2.direction = Direction.INPUT
        self._b2.pull = Pull.UP
        # B3
        self._b3 = DigitalInOut(board.D15)
        self._b3.direction = Direction.INPUT
        self._b3.pull = Pull.UP
        # B4
        self._b4 = DigitalInOut(board.D16)
        self._b4.direction = Direction.INPUT
        self._b4.pull = Pull.UP


    ######################################################
    #   Buzzer and Rumbler
    ######################################################
    def buzz(self, duration):
        '''
        Buzzes for a set duration. This only works if you have the physical 
        game pad switch set to software mode.

        duration (float) = the number of seconds you want to play the tone

        examples:
            buzz(0.5)
            buzz(1.0)
            buzz(2.2)
        '''

        duration = max(0.1, duration)

        self._buzzer_rumbler.value = False      # Buzzer On
        time.sleep(duration)
        self._buzzer_rumbler.value = True       # Buzzer Off


    ######################################################
    #   Sensors
    ######################################################
    @property
    def x_voltage(self):    # Joystick X axis - Voltage
        return 1.0 - ((self._joystick_x.value * 3.3) / 65536)

    @property
    def y_voltage(self):    # Joystick Y axis - Voltage
        return (self._joystick_y.value * 3.3) / 65536

    @property
    def x(self):    # Joystick X axis - Value from 0.0 to 1.0
        return 1.0 - (self._joystick_x.value / 65536)

    @property
    def y(self):    # Joystick Y axis - Value from 0.0 to 1.0
        return self._joystick_y.value / 65536

    @property
    def press(self):    # Joystick Button - Value (True/False)
        return not self._joystick_press.value

    @property
    def b1(self):   # B1 Button - Value (True/False)
        return not self._b1.value

    @property
    def b2(self):   # B2 Button - Value (True/False)
        return not self._b2.value

    @property
    def b3(self):   # B3 Button - Value (True/False)
        return not self._b3.value

    @property
    def b4(self):   # B4 Button - Value (True/False)
        return not self._b4.value

gamepad = Game_Pad()

# CircuitPython Clue Controller
# Last Updated Dec. 27, 2020
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
jisforjt_controller.py:
v1
    This is a higher-level library to allow Adafruit's CLUE and Yahboom's micro:bit 
    Game Controller to communicate while maintaining all the functionality of the CLUE, 
    except for touch features.
'''

######################################################
#   Pin Reference
######################################################
"""
Pins
    P0  -Digital    Controller Buzzer
    P1  -Analog     Controller - Joystick: X
    P2  -Analog     Controller - Joystick: Y
    P5  -Digital    Clue Button A
    P8  -Digital    Controller - Joystick: Press
    P11 -Digital    Clue Button B
    P13 -Digital    Controller - Button B1
    P14 -Digital    Controller - Button B2
    P15 -Digital    Controller - Button B3
    P16 -Digital    Controller - Button B4
    P17 -Digital    Clue LED
    P18 -Digital    Clue Neopixel
    P43 -Digital    Clue White LEDs
"""


######################################################
#   Import
######################################################
import time
import board
import pulseio
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn

import array
import math

try:
    from audiocore import RawSample
except ImportError:
    from audioio import RawSample
 
try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

class Controller:

    def __init__(self):

        # Define sound and rumble
        self._buzzer_rumbler = DigitalInOut(board.P0)
        self._buzzer_rumbler.direction = Direction.OUTPUT
        self._buzzer_rumbler.value = True

        # Define joystick pins
        self._joystick_x = AnalogIn(board.P1)
        self._joystick_y = AnalogIn(board.P2)
        
        # Define Buttons
        # Joystick Press
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
    #   Sounds and Rumbles
    ######################################################
    def playTone(self, duration):
        '''
        Plays a tone for a set duration.

        tone (integer) =  the frequency of the tones/music notes you want to play
        duration (float) = the number of seconds you want to play the tone
         
            tone     music note
            262    =     C4
            294    =     D4
            330    =     E4
            349    =     F4
            392    =     G4
            440    =     A4
            494    =     B4

        examples:
            playTone(294, 0.5)
            playTone(349, 1.0)
            playTone(440, 2.2)
        '''

        duration = max(0.1, duration)

        self._buzzer_rumbler.value = False
        time.sleep(duration)
        self._buzzer_rumbler.value = True


    ######################################################
    #   Sensors
    ######################################################
    @property
    def x_Voltage(self):
        return (self._joystick_x.value * 3.3) / 65536

    @property
    def y_Voltage(self):
        return (self._joystick_y.value * 3.3) / 65536

    @property
    def x(self):
        return self._joystick_x.value / 65536

    @property
    def y(self):
        return self._joystick_y.value / 65536

    @property
    def press(self):
        return not self._joystick_press.value

    @property
    def b1(self):
        return not self._b1.value

    @property
    def b2(self):
        return not self._b2.value

    @property
    def b3(self):
        return not self._b3.value

    @property
    def b4(self):
        return not self._b4.value

    @property
    def buzz(self):
        return self._buzzer_rumbler.value

controller = Controller()

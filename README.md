# CircuitPython_CLUE_Yahboom_Game_Pad
This is a higher-level library to allow Adafruit's [CLUE](https://www.adafruit.com/product/4500) and Yahboom's Micro:bit Compact [Game Pad](http://www.yahboom.net/study/SGH) to communicate while maintaining all the functionality of the CLUE, except for touch features.

## Dependencies
This library depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython) v.6.3.0

The test example also depends on:
* [Adafruit_CLUE*](https://github.com/adafruit/Adafruit_CircuitPython_CLUE) v.3.0.0

The Egg Quest game example also depends on:
* [Adafruit_CLUE*](https://github.com/adafruit/Adafruit_CircuitPython_CLUE) v.3.0.0
* [Adafruit Imangeload*](https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad) v.1.15.1
* [Adafruit Display Text*](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text) v.2.20.0

*All repositories are available in the Circuitpython Bundle v.6.X


## Instalations
Follow Adafruit's [CLUE Overview](https://learn.adafruit.com/adafruit-clue) instructions under _CircuitPython on CLUE_. During the installation process, you will download the latest _library bundle_ and transfer several libraries to the CLUE. Transfer the dependencies listed above to your _lib folder_.
Download this repository and copy _jisforjt_cutebot_clue.mpy_ on to your CIRCUITPY drive. The _.mpy_ version of the files uses a fraction of the memory and is the reccommended version.

## Usage
You can create a new main.py file and use:
```python
from jisforjt_controller import controller
```

## License
The code of the repository is made available under the terms of the MIT license. See license.md for more information.

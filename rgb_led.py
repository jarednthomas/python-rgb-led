#!/usr/bin/env python3
"""
rgb_led.py
~~~~~~~~

Python based script that cycles through RGB Colors using a Raspberry Pi
"""

import os
import time
import RPi.GPIO as GPIO
from datetime import datetime

# Pins (BCM) https://pinout.xyz/
button_pin = 4
red_pin = 25
green_pin = 24
blue_pin = 23

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Variables
light_code = 0
buttonPressedTime = None

def buttonStateChanged(pin):
    """ Defines Button Press Event """
    global buttonPressedTime
    global light_code

    if not (GPIO.input(pin)):
        if buttonPressedTime is None:
            buttonPressedTime = datetime.now()

    else:
        if buttonPressedTime is not None:

            light_code += 1
            if light_code == 8:
                light_code = 0
                
            if light_code == 0: # OFF
                GPIO.output(red_pin, False)
                GPIO.output(green_pin, False)
                GPIO.output(blue_pin, False)
                
            elif light_code == 7: #RGB = WHITE
                GPIO.output(red_pin, True)
                GPIO.output(green_pin, True)
                GPIO.output(blue_pin, True)
                
            elif light_code == 6: #BG = CYAN
                GPIO.output(red_pin, False)
                GPIO.output(green_pin, True)
                GPIO.output(blue_pin, True)
                
            elif light_code == 5: #RB = PURPLE
                GPIO.output(red_pin, True)
                GPIO.output(green_pin, False)
                GPIO.output(blue_pin, True)
                
            elif light_code == 4: #RG = YELLOW
                GPIO.output(red_pin, True)
                GPIO.output(green_pin, True)
                GPIO.output(blue_pin, False)
                
            elif light_code == 3: # BLUE
                GPIO.output(red_pin, False)
                GPIO.output(green_pin, False)
                GPIO.output(blue_pin, True)
                
            elif light_code == 2: # GREEN
                GPIO.output(red_pin, False)
                GPIO.output(green_pin, True)
                GPIO.output(blue_pin, False)
                
            elif light_code == 1: # RED
                GPIO.output(red_pin, True)
                GPIO.output(green_pin, False)
                GPIO.output(blue_pin, False)
                
            buttonPressedTime = None

try:
    print("[RGB_LED Active] CTRL-C to Quit")
    GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=buttonStateChanged)
    while True:
        time.sleep(1) # sleep to reduce CPU usage

except KeyboardInterrupt:
    print("\n")

finally:
    GPIO.output(red_pin, False)
    GPIO.output(green_pin, False)
    GPIO.output(blue_pin, False)
    GPIO.cleanup()

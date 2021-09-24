#!/usr/bin/python

# https://github.com/astro-pi/python-sense-hat/blob/master/examples/compass.py

## Dokumentation af import
import sys
from os import environ

if 'EMU' in environ and environ['EMU']:
    from sense_emu import SenseHat
else:
    from sense_hat import SenseHat

## Pipenv indlæser automatisk .env ved start med `pipenv shell` og `pinenv run`.
## Dermed kan EMU defineres i .env og dermed bestemme om vi skal importere sense_emu eller sense_hat


# To get good results with the magnetometer you must first calibrate it using
# the program in RTIMULib/Linux/RTIMULibCal
# The calibration program will produce the file RTIMULib.ini
# Copy it into the same folder as your Python code

## 
# en matrix, foldet ud som en en-dimensionel array, af grader for kompaset
led_loop = [4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8, 0, 1, 2, 3]

## snese er objektet
# SenseHat obejektet
sense = SenseHat()
sense.set_rotation(0)

# Slet alle LED'er
sense.clear()

sense.set_imu_config(True, False, False) # sense.set_imu_config(compass_enabled, gyro_enabled, acc_enabled)

## Forrige x
# 
prev_x = 0

## Forrige y
prev_y = 0


led_degree_ratio = len(led_loop) / 360.0

while True:
    dir = sense.get_compass()
    print("North: %s" % dir)
    dir_inverted = 360 - dir  # So LED appears to follow North
    led_index = int(led_degree_ratio * dir_inverted)
    led_index = led_index % 28
    offset = led_loop[led_index]

    y = offset // 8  # row
    x = offset % 8  # column

    if x != prev_x or y != prev_y:
        sense.set_pixel(prev_x, prev_y, 0, 0, 0)

    sense.set_pixel(x, y, 0, 0, 255)

    prev_x = x
    prev_y = y


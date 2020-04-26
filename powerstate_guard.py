#! /usr/bin/env python3

import RPi.GPIO as GPIO
import obdl.config as config
import os,time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(config.powerstate_pin, GPIO.IN)

while True:
    time.sleep(0.1)
    if not GPIO.input(config.powerstate_pin):
        os.system("shutdown -h now")


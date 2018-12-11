#! /home/thibault/.virtualenvs/obd/bin/python3

import RPi.GPIO as GPIO
import obdl.config as config
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(config.watchdog_pin, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(config.activity_pin, GPIO.OUT, initial=GPIO.HIGH)

while True:
    GPIO.output(config.watchdog_pin, not GPIO.input(config.watchdog_pin))
    GPIO.output(config.activity_pin, not GPIO.input(config.activity_pin))
    time.sleep(.1)

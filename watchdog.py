#! /home/thibault/.virtualenvs/obd/bin/python3

import RPi.GPIO as GPIO
import obdl.config as config

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(config.watchdog_pin, GPIO.OUT, initial=GPIO.LOW)

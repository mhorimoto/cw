#! /usr/bin/env python3
#
import orangepi.one
import OPi.GPIO as GPIO
import time

dot = 0.33333333
mark = dot * 3
space = dot * 3
between_dot = dot/3

# GPIO.setmode(GPIO.SUNXI)
# GPIO.setwarnings(False)
# GPIO.setup("PC7",GPIO.OUT,0)
# GPIO.setwarnings(True)
# GPIO.output("PC7",1)
# time.sleep(1)
# GPIO.output("PC7",0)


def light_up(sec):
#    GPIO.setwarnings(False)
#    GPIO.setup("PC7",GPIO.OUT)
#    GPIO.setwarnings(True)
    GPIO.output("PC7",GPIO.HIGH)
    time.sleep(sec)
    GPIO.output("PC7",GPIO.LOW)
#    GPIO.cleanup()

def light_down(sec):
#    GPIO.setmode(GPIO.SUNXI)
#    GPIO.setwarnings(False)
#    GPIO.setup("PC7",GPIO.OUT)
#    GPIO.setwarnings(True)
    GPIO.output("PC7",GPIO.LOW)
    time.sleep(sec)
#    GPIO.cleanup()


GPIO.setmode(GPIO.SUNXI)
GPIO.setup("PC7",GPIO.OUT)
text = "...- ...- ...- "
for c in text:
    if c == '.':
        light_up(dot)
    if c == '-':
        light_up(mark)
    if c == ' ':
        light_down(space)
    time.sleep(between_dot)

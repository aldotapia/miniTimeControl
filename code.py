# coding=utf-8


import board
import digitalio
import time
import simpleio

# select pins for leds
greenpin = board.D5
yellowpin = board.D7
redpin = board.D9
buzzer_pin = board.D3

# set up calls
first_call = 10*60
last_call = 15*60
# delay time is for led blinking before each call
delay = 60

# set
green = digitalio.DigitalInOut(greenpin)
green.direction = digitalio.Direction.OUTPUT
green.value = False
yellow = digitalio.DigitalInOut(yellowpin)
yellow.direction = digitalio.Direction.OUTPUT
yellow.value = False
red = digitalio.DigitalInOut(redpin)
red.direction = digitalio.Direction.OUTPUT
red.value = False


# function to blink leds at the start
def fancy_start(green, yellow, red):
    green.value = True
    time.sleep(0.1)
    yellow.value = True
    time.sleep(0.1)
    green.value = False
    red.value = True
    time.sleep(0.1)
    yellow.value = False
    time.sleep(0.1)
    red.value = False


for i in range(0, 5):
    fancy_start(green, yellow, red)

start = time.monotonic()
current = time.monotonic()
green.value = True
flag = True
simpleio.tone(buzzer_pin, 264, duration=0.5)

while (current - start) < (first_call - delay):
    time.sleep(0.2)
    current = time.monotonic()

# blink before first call
while (current - start) < first_call:
    green.value = False
    yellow.value = True
    time.sleep(0.2)
    green.value = True
    yellow.value = False
    time.sleep(0.2)
    current = time.monotonic()

green.value = False
yellow.value = True

# first call
while (current - start) < (last_call - delay):
    if flag:
        simpleio.tone(buzzer_pin, 264, duration=1.0)
    time.sleep(0.2)
    current = time.monotonic()
    flag = False

# blink before last call
while (current - start) < last_call:
    yellow.value = False
    red.value = True
    time.sleep(0.2)
    yellow.value = True
    red.value = False
    time.sleep(0.2)
    current = time.monotonic()

# last call
yellow.value = False
red.value = True
simpleio.tone(buzzer_pin, 264, duration=2.0)

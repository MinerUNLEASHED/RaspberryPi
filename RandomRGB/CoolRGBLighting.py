from picozero import RGBLED
from time import sleep
from random import randint

rgb = RGBLED(red=1, green=2, blue=3)
rgb.on()


def newRand():
    return randint(0, 255)


while True:
    rgb.color = (newRand(), newRand(), newRand())
    sleep(0.1)

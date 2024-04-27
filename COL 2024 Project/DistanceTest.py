from gpiozero import LED, Button
from time import sleep
from signal import pause

button = Button(15)
button2 = Button(13)
Redled = LED(2)
Greenled = LED(4)

def press():
    Redled.on()
    Greenled.off()

def rel():
    Redled.off()
    Greenled.on()

def boP():
    Redled.on()
    Greenled.on()

def boR():
    Redled.off()
    Greenled.off()

button.when_pressed = press
button.when_released = rel
button2.when_pressed = boP
button2.when_released = boR

pause()




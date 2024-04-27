from gpiozero import LED, Button
from time import sleep

button = Button(15)
Redled = LED(2)
Greenled = LED(4)

def press():
    Redled.on()
    Greenled.off()

def rel():
    Redled.off()
    Greenled.on()

button.when_pressed = press
button.when_released = rel





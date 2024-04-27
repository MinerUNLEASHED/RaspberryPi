from gpiozero import LED
from time import sleep
Redled = LED(2)
Greenled = LED(4)

while True:
    Redled.on()
    Greenled.off()
    sleep(1)
    Redled.off()
    Greenled.on()
    sleep(0.5)



from gpiozero import DistanceSensor, LED
Redled = LED(2)
Greenled = LED(4)

while True:
    Redled.on()
    Greenled.off()

    Redled.off()
    Greenled.on()




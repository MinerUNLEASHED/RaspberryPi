from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=15, trigger=14)
while True:
    print(ultrasonic.distance)
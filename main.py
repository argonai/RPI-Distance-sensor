# Write your code here :-)
import time
import voorbeeld
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

Trigger_output = 11
Echo_input = 13

sleeptime = 0.8

GPIO.setup(Trigger_output, GPIO.OUT)
GPIO.setup(Echo_input, GPIO.IN)
GPIO.output(Trigger_output, False)
print("waiting")
try:
    while True:
    
        GPIO.output(Trigger_output, True)
        time.sleep(0.00001)
        GPIO.output(Trigger_output, False)
        turn_on_time = time.time()
        while GPIO.input(Echo_input) == 0:
            turn_on_time = time.time()
        while GPIO.input(Echo_input) == 1:
            break_time = time.time()

        time_amount = break_time - turn_on_time
        distance = (time_amount * 34300) / 2
        #distance = time_amount

        #if(distance < 2 or (round(distance)>300)):
         #   print("Distance out of range")
        #else:
        print(f"Distance is: {distance} cm")

        time.sleep(sleeptime)
finally:
    print("clean up")
    GPIO.cleanup()
# Write your code here :-)
from vlc import Instance
import os
import time
import RPi.GPIO as GPIO
from random import randint
GPIO.setmode(GPIO.BOARD)

Trigger_output = 11
Echo_input = 13

sleeptime = 0.8
random_vid = 0
GPIO.setup(Trigger_output, GPIO.OUT)
GPIO.setup(Echo_input, GPIO.IN)
GPIO.output(Trigger_output, False)
print("waiting")
trigger_prevent = 0

class VLC:
    def __init__(self):
        self.Player = Instance()

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        #uncoment de lijn 25 en verander de path naar de folder met de gedichten
        path = r"/home/pi/RPI-Distance-sensor/vids" 
        songs = os.listdir(path)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path,s)))
        self.listPlayer = self.Player.media_list_player_new()
        self.listPlayer.set_media_list(self.mediaList)
    def play(self):
        self.listPlayer.play()
    def next(self):
        self.listPlayer.next()
    def pause(self):
        self.listPlayer.pause()
    def previous(self):
        self.listPlayer.previous()
    def stop(self):
        self.listPlayer.stop()
player = VLC()
player.addPlaylist()
player.play()
time.sleep(2)
player.pause()
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

        if(distance < 2 or (round(distance)>200)):
            print(distance)
            print("Distance out of range")
        else:
            print(f"Distance is: {distance} cm")
        
        
        if(trigger_prevent == 0 and distance < 130):
            trigger_prevent = 1
            player.next()
        elif(trigger_prevent == 1 and distance > 130):
            player.pause()
            trigger_prevent = 0
       
            
        
            
       
            
    
    
        time.sleep(sleeptime)
finally:
    print("clean up")
    GPIO.cleanup()
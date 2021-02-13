
#from pynput.keyboard import Key, Listener
import keyboard
import time
import VL53L0X
 
# Create a VL53L0X object
tof = VL53L0X.VL53L0X()
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
 
# Evento di pressing
while(True):
    #print (keyboard.is_pressed("space"))

    if(keyboard.is_pressed("space")):
         print ("capturing..")
         #tof = VL53L0X.VL53L0X()
         #tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
         distance = tof.get_distance()
         if (distance > 0):
              print ("%d mm" % distance)
tof.stop_ranging()


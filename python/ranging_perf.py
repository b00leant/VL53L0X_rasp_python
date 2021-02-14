
#from pynput.keyboard import Key, Listener
import keyboard
import time
import VL53L0X
 
# Create a VL53L0X object
tof = VL53L0X.VL53L0X()
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)


perf = tof.perf_single_m()
print (perf)

 
# Evento di pressing
#while(True):
    #print (keyboard.is_pressed("space"))

    #if(keyboard.is_pressed("space")):
         #print ("capturing..")
         #tof = VL53L0X.VL53L0X()
         #tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
         #distance = tof.get_distance()
    #perf = tof.perf_single_m()
    #print (perf)
    #time.sleep(1)
tof.stop_ranging()


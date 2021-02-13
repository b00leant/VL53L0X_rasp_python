from pynput.keyboard import Key, Listener
import time
import VL53L0X
 
# Create a VL53L0X object
tof = VL53L0X.VL53L0X()
 
# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)
 
timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))
 
for count in range(1,1001):
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm" % distance)
 
    time.sleep(timing/1000000.00)
 
tof.stop_ranging()

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()

import PyDynamixel_v2 as pd
import cv2
from time import sleep

# Declare the DxlComm variable
port = "/dev/ttyUSB0"
baudrate = 57600
serial = pd.DxlComm(port=port, baudrate=baudrate)

# Declare a dynamixel joint
dyn_id1 = 1
dyn_id2 = 2
dyn_id3 = 3
dyn_id4 = 4
dyn_id5 = 5
dyn_id6 = 6
dyn_id7 = 19
dyn_id8 = 20

dyn1 = pd.Joint(dyn_id1)
dyn2 = pd.Joint(dyn_id2)
dyn3 = pd.Joint(dyn_id3)
dyn4 = pd.Joint(dyn_id4)
dyn5 = pd.Joint(dyn_id5)
dyn6 = pd.Joint(dyn_id6)
dyn7 = pd.Joint(dyn_id7)
dyn8 = pd.Joint(dyn_id8)


print("Attach joint")
serial.attach_joints([dyn1, dyn2, dyn3, dyn4, dyn5, dyn6, dyn7, dyn8])
# You could also send all joints as a list to DxlComm varible
# serial.attach_joints([dyn, dyn2, dyn3])

# Enable single joint torque or all joints torques
print("Disable torque")
serial.disable_torques()

sleep(2)

dyn1.reboot()
dyn2.reboot()
dyn3.reboot()
dyn4.reboot()
dyn5.reboot()
dyn6.reboot()
dyn7.reboot()
dyn8.reboot()

serial.release()
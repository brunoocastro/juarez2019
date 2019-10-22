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
dyn_id7 = 7
dyn_id8 = 8
dyn_id9 = 9
dyn_id10 = 10
dyn_id11 = 11
dyn_id12 = 12
dyn_id13 = 13
dyn_id14 = 14
dyn_id15 = 15
dyn_id16 = 16
dyn_id17 = 17
dyn_id18 = 18
dyn_id19 = 19
dyn_id20 = 20


dyn1 = pd.Joint(dyn_id1)
dyn2 = pd.Joint(dyn_id2)
dyn3 = pd.Joint(dyn_id3)
dyn4 = pd.Joint(dyn_id4)
dyn5 = pd.Joint(dyn_id5)
dyn6 = pd.Joint(dyn_id6)
dyn7 = pd.Joint(dyn_id7)
dyn8 = pd.Joint(dyn_id8)
dyn9 = pd.Joint(dyn_id9)
dyn10 = pd.Joint(dyn_id10)
dyn11 = pd.Joint(dyn_id11)
dyn12 = pd.Joint(dyn_id12)
dyn13 = pd.Joint(dyn_id13)
dyn14 = pd.Joint(dyn_id14)
dyn15 = pd.Joint(dyn_id15)
dyn16 = pd.Joint(dyn_id16)
dyn17 = pd.Joint(dyn_id17)
dyn18 = pd.Joint(dyn_id18)
dyn19 = pd.Joint(dyn_id19)
dyn20 = pd.Joint(dyn_id20)


print("Attach joint")
serial.attach_joints([dyn1, dyn2, dyn3, dyn4, dyn5, dyn6, dyn7, dyn8, dyn9, dyn10, dyn11, dyn12, dyn13, dyn14, dyn15, dyn16, dyn17, dyn18, dyn19, dyn20])
# You could also send all joints as a list to DxlComm varible
# serial.attach_joints([dyn, dyn2, dyn3])

# Enable single joint torque or all joints torques
print("Disable torque")
serial.disable_torques()

sleep(2)

print("Rebooting motors")
dyn1.reboot()
dyn2.reboot()
dyn3.reboot()
dyn4.reboot()
dyn5.reboot()
dyn6.reboot()
dyn7.reboot()
dyn8.reboot()

serial.release()
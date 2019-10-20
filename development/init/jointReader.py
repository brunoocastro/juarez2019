import PyDynamixel_v2 as pd
import cv2
from time import sleep
import sys

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

# Attach this joint to DxlComm to enable serial communication
print("Attach joint")
serial.attach_joints([dyn1, dyn2, dyn3, dyn4, dyn5, dyn6, dyn7, dyn8])
# You could also send all joints as a list to DxlComm varible
# serial.attach_joints([dyn, dyn2, dyn3])


# Enable single joint torque or all joints torques
#print("Enable torque")
serial.disable_torques()

sleep(2)

def printer():
    print(
        "\n----------------------------------------------------" +
        " \nPress C to return\n " +
        "\nID 1 - Current angle: {}\n".format(dyn1.get_angle()) +
        "ID 2 - Current angle: {}\n".format(dyn2.get_angle()) +
        "ID 3 - Current angle: {}\n".format(dyn3.get_angle()) +
        "ID 4 - Current angle: {}\n".format(dyn4.get_angle()) +
        "ID 5 - Current angle: {}\n".format(dyn5.get_angle()) +
        "ID 6 - Current angle: {}\n".format(dyn6.get_angle()) +
        "ID 19 - Current angle: {}\n".format(dyn7.get_angle()) +
        "ID 20 - Current angle: {}\n".format(dyn8.get_angle()) +
        "----------------------------------------------------\n" 
        )

while True:
    print("-------------------------------------------")
    print("\nD - Disable all torques\nE - Enable all torques\nP - Position Printer\nF - Finish the program\n")
    print("-------------------------------------------")\
        #Z - Type an id to DISABLE torque\nX - Type an id to ENABLE torque

    opt = raw_input("Digite uma opcao para o menu: ")
    print("\n")

    if opt == "d" or opt == "D":
        # Disable all or single joints torques
        print("Disable all top torques")
        serial.disable_torques() # all joints

    elif opt == "e" or opt == "E": 
        # Disable all or single joints torques
        print("Enable all top torques")
        serial.enable_torques() # all joints

    elif opt == "p" or opt == "P": 
        # Disable all or single joints torques
        print(" Printer ")
        printer()

    elif opt == "f" or opt == "F":
        print("Closing")
        sys.exit(0)

    else:
        print("Invalid Option")
        pass

        sleep (0.5)

        '''
    elif opt == "z" or opt == "Z":
        # Disable all or single joints torques
        val = int(input("[D] - ID do motor: "))

        print("ID[{}] - Disable Torque")
        serial.disable_torque(val) # all joints

    elif opt == "x" or opt == "X":
        # Disable all or single joints torques
        val = str(input("[E] - ID do motor: "))

        print("ID[{}] - Disable Torque".format(val))
        V = (dyn1, dyn2, dyn3, dyn4, dyn5, dyn6, dyn7, dyn8)
        V[val].enable_torque(val) # all joints 
    '''
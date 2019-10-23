import rospy
from robotis_controller_msgs.srv import SetJointModule
from std_msgs.msg import String


params = SetJointModule()

params.joint_name = ['r_hip_yaw', 'r_hip_roll', 'r_hip_pitch', 'r_knee', 'r_ankle_pitch', 'r_ankle_roll', 'l_hip_yaw', 'l_hip_roll', 'l_hip_pitch', 'l_knee', 'l_ankle_pitch', 'l_ankle_roll']
params.module_name = ['walking_module','walking_module','walking_module','walking_module','walking_module','walking_module','walking_module','walking_module','walking_module','walking_module','walking_module']

rospy.Service('robotis/set_present_joint_ctrl_modules', SetJointModule, a)#, self.queue_size)

pub = rospy.Publisher('robotis/walking/command', String, queue_size=10)
pub.publish("walking")

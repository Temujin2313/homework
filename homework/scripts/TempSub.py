#!/usr/bin/env python3
# This is the listener node and will subscribe to the chatter topic


#from my_msgs.msg import Floats
#from rospy.numpy_msg import numpy_msg
import rospy
from std_msgs.msg import Float32MultiArray
import matplotlib.pyplot as plt
def my_charter_callback(message):
    plt.plot(message.data)
    plt.show()
    #rospy.loginfo( "%f:" , message.data[1])

def my_listener():
    rospy.init_node('Plot_data', anonymous=True)

    rospy.Subscriber('temp_data', Float32MultiArray, my_charter_callback) # Subscriber object

    rospy.spin() # Program will enter the listening mode and execute the call back function

if __name__ == '__main__':
    my_listener()
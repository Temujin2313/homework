#!/usr/bin/env python3

import rospy
#from scripts.Cord import pos_callback
#from homework.msg import TempData
from std_msgs.msg import Float32MultiArray
from numpy import random
import time


# Define the talker fuction
def my_talker():

    pub = rospy.Publisher('temp_data', Float32MultiArray, queue_size=10)
    rospy.init_node('temp_Sensor_node', anonymous=True) # Tell ROSpy this is a node. Anonymous Ture create different ID for different node with same name
    message = Float32MultiArray()
    rate = rospy.Rate(1) # 1 hz. How oftern we are sending

    message.data = []
    for j in range(10):
        rate.sleep()
        message.data.append(random.randint(35,90))
        #message.data = [random.randint(35,90)]
        #IoTmessage.name = 'my_sensor'
        #IoTmessage.temperature = 25 + random.rand()*3
        #IoTmessage.humidity = 45 + random.rand()*2
        rospy.loginfo(message)
    pub.publish(message)

if __name__ == '__main__':
    try:
        my_talker()
    except rospy.ROSInitException:
        pass

 
    
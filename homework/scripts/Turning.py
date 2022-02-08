#!/usr/bin/env python3


from hashlib import new
import rospy
from turtlesim.msg import Pose
import turtlesim
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import time
import math
import numpy as np
import turtle
from std_srvs.srv import Empty

x = 0
y = 0
yaw = 0



#def read_turtle_pos():

   # rospy.Subscriber('/turtle1/pose',Pose,pos_callback)

def pos_callback(message):
    # print('x = %f' % message.x)
    # print('y = %f' % message.y)
    # print('theta = %f' % message.theta)
    # print('linear_velocity = %f' % message.linear_velocity)
    # print('angular_velocity = %f' % message.angular_velocity)
    global x,y,yaw
    x = message.x
    y = message.y
    yaw = message.theta


    


def Turn(speed,arra):
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    
    loop_rate = rospy.Rate(10)
    
    targetX = 0
    targetY = 0


    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

    while True:

        velocity_message.angular.z = (arra-yaw)
        velocity_publisher.publish(velocity_message)

        print(yaw)
        
        if abs((arra - yaw)) < (.001):
            #print("Radians to turn", MyRadians)
            print("Done", x ,y, yaw)
            velocity_message.angular.z = 0      
            velocity_publisher.publish(velocity_message)

            break

        loop_rate.sleep()

    
        
           
if __name__ == '__main__':
    #rospy.wait_for_service('turtle1/teleport_absolute')
    try:
        #rospy.wait_for_service('reset')
        #reset_turtle = rospy.ServiceProxy('reset', Empty)
        #reset_turtle()
        resT = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
        resT2 = resT(5.544445,5.544445,0)
        rospy.init_node("turn_around", anonymous=True)
        rospy.Subscriber('/turtle1/pose',Pose,pos_callback)
       
        time.sleep(2)

        t = -2
        Turn(1,t)
        time.sleep(2)
        rospy.spin()


    except rospy.ROSInternalException:
        pass
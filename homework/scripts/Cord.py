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


def Move(speed,arra):
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    loop_rate = rospy.Rate(10)
    x0 = arra[0]
    y0 = arra[1]
    x1 = x
    y1 = y
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size =100)
    distance = abs((math.sqrt((x0-x)**2+(y0 - y)**2)))
    print("Distance to move", distance)
    while True:
        #rospy.loginfo("Turtlesim moving forward")
        velocity_message.linear.x = speed
        velocity_publisher.publish(velocity_message)
        
        loop_rate.sleep()
        distance_moved = abs((math.sqrt((x-x1)**2+(y-y1)**2)))
        #print("Distance moved", distance_moved)
        #print('x and y   ', x, y)
        if not (distance_moved < distance):
            print("Distance moved", distance_moved)
            print('x and y   ', x, y)
            rospy.loginfo("Reached")
            break
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)    


def Turn(speed,arra):
    velocity_message = Twist()
    velocity_message.linear.x = 0
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    
    loop_rate = rospy.Rate(10)
    
    targetX = arra[0]
    targetY = arra[1]

    MyRadians =  math.atan2(targetY - y, targetX - x)
    MyRadians2 = math.atan2(targetY - y, targetX - x)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    print("MyRadians", math.atan2(targetY - y, targetX - x))
    print("abs of Myradians " ,abs(MyRadians))
    print("MyRadians2 ", MyRadians2)
    print("Abs of MyRadians2", abs(MyRadians2))
    loops = 0
    if MyRadians < 0 :
        MyRadians = MyRadians
    # else:
    #     MyRadians = MyRadians
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

    while True:

        velocity_message.angular.z = (MyRadians-yaw)
        velocity_publisher.publish(velocity_message)

        print(yaw)
        
        if abs((MyRadians - yaw)) < (.001):
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
        rospy.init_node("go_to_goal", anonymous=True)
        rospy.Subscriber('/turtle1/pose',Pose,pos_callback)
       
        time.sleep(2)
        t = ([7,6], [4,2], [9,5], [3,1], [5,8])
        
        for i in t:
            Turn(1,i)
            time.sleep(2)
            Move(1,i)
            time.sleep(2)
        rospy.spin()


    except rospy.ROSInternalException:
        pass
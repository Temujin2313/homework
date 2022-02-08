#!/usr/bin/env python3


import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import time
import math


x = 0
y = 0
yaw = 0

def read_turtle_pos():

    
    rospy.Subscriber('/turtle1/pose',Pose,pos_callback)
    

def pos_callback(message):
    print('x = %f' % message.x)
    print('y = %f' % message.y)
    print('theta = %f' % message.theta)
    print('linear_velocity = %f' % message.linear_velocity)
    print('angular_velocity = %f' % message.angular_velocity)
    global x,y,yaw
    x = message.x
    y = message.y
    yaw = message.theta


def move(speed,distance):
    velocity_message = Twist()
    velocity_message.linear.x = speed
    velocity_message.linear.y = 0
    velocity_message.linear.z = 0
    velocity_message.angular.x = 0
    velocity_message.angular.y = 0
    velocity_message.angular.z = 0
    loop_rate = rospy.Rate(10)
    x0 = x
    y0 = y
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size =10)

    while True:
        rospy.loginfo("Turtlesim moving forward")
        velocity_publisher.publish(velocity_message)
        loop_rate.sleep()
        distance_moved = abs((math.sqrt((x0-x)**2+(y0-y)**2)))
        print(distance_moved)
        if not (distance_moved < distance):
            rospy.loginfo("Reached")
            break
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

if __name__ == '__main__':
    try:
        rospy.init_node("draw_StraightLine", anonymous=True)
        read_turtle_pos()
        time.sleep(2)
        move(1,3)
        rospy.spin()
    except rospy.ROSInternalException:
        pass


#/turtle1/cmd_vel
# ros message type  geometry_msgs/Twist
# geometry_msgs/Vector3 linear
#   float64 x
#   float64 y
#   float64 z
# geometry_msgs/Vector3 angular
#   float64 x
#   float64 y
#   float64 z

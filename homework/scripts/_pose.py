#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def read_turtle_pos():

    rospy.init_node("read_turtle_pos", anonymous=True)
    rospy.Subscriber('/turtle1/pose',Pose,pos_callback)
    rospy.spin()

def pos_callback(message):
    print('x = %f' % message.x)
    print('y = %f' % message.y)
    print('theta = %f' % message.theta)
    print('linear_velocity = %f' % message.linear_velocity)
    print('angular_velocity = %f' % message.angular_velocity)

if __name__ == '__main__':
    try:
        read_turtle_pos()
    except rospy.ROSInternalException:
        pass
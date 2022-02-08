#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
#from homework.msg import DrawCircle
import sys


def turtle_circle(radius):
	rospy.init_node("DrawCircle", anonymous= True)
	pub = rospy.Publisher('/turtle1/cmd_vel',
						Twist, queue_size=10)
	vel = Twist()
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		vel.linear.x = radius
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1
		rospy.loginfo("Radius = %f",
					radius)
		pub.publish(vel)
		rate.sleep()

def KeyBoard():
	radius = input("Please input a radius ")
	return int(radius)

if __name__ == '__main__':
	try:
	
		radius = KeyBoard()   
		turtle_circle(radius)
	except rospy.ROSInterruptException:
		pass

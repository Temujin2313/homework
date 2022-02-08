#!/usr/bib/env python
"""This code will publish a command to move the turtle sim in a straghtline. 
We will subscribe the turtlesim/pose message for the updated position of 
the robot. Then calculate the distrance travelled.
"""

from cmath import pi
from signal import pause
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class move(object):
    
    def __init__(self):
        # Initialize the pose values of the turtel sim
        self.x = 0
        self.y = 0
        self.z = 0
        
        # Creater a publisher
        self.vel_topic = '/turtle1/cmd_vel'
        self.velocity_publisher = rospy.Publisher(self.vel_topic, Twist, queue_size=10)
        # Create the subscriber
        self.pose_topic = '/turtle1/pose'
        self.pose_subscriber = rospy.Subscriber(self.pose_topic, Pose, self.pose_callback)
        rospy.sleep(2)
        self.loop_rate = rospy.Rate(10)



    def pose_callback(self, pose_msg):
        self.x = pose_msg.x
        self.y = pose_msg.y
        self.z = pose_msg.theta
        #rospy.loginfo('linear_x = %f'%self.x)
        #rospy.loginfo('Linear_y = %f'%self.y)
        



    def move_straight(self, speed, distance):

        # set the initial value of the position
        x0 = self.x
        y0 = self.y
        rospy.loginfo("Initial X0  and Y0 = %f and %f" % (x0, y0))



        # Create an object for the Twist message
        linear_velocity = Twist()

        # Set the speed of the turtlesim
        

        distance_moved = 0
        
        while True:
            linear_velocity.linear.x = speed
            rospy.loginfo('Turtlesim is moving in straightline')
            self.velocity_publisher.publish(linear_velocity)
            
            # Calucate the distance moved using Ecludian distance
            distance_moved = abs((math.sqrt((self.x - x0)**2 + (self.y - y0)**2)))
            rospy.loginfo("Distace travelled = %f" % distance_moved)
            self.loop_rate.sleep()

            if not (distance_moved < distance):
                rospy.loginfo("Reached Destination")
                break
        linear_velocity.linear.x = 0
        self.velocity_publisher.publish(linear_velocity)





    def move_angular(self, velocity, angle_deg):
        print('Starting rotation')

        angular_velocity = Twist()
        z0 = self.z
        
        angular_velocity.angular.z = velocity
        t0 = rospy.Time.now().to_sec()

        while True:
            rospy.loginfo('Turtlesim turing its head')
            self.velocity_publisher.publish(angular_velocity)
            self.loop_rate.sleep()

            t1 = rospy.Time.now().to_sec()
            angle_moved = (180/math.pi)*abs(velocity*(t1-t0))

            if not(angle_moved<angle_deg):
                rospy.loginfo("Turned the desired angle")
                break
            
        angular_velocity.angular.z = 0
        self.velocity_publisher.publish(angular_velocity)

    def go_destination(self, x_des, y_des):
        velocity_message = Twist()
        # Find the distance and desired heading
        while True:
            try:
                distance = abs(math.sqrt((x_des - self.x)**2 + (y_des - self.y)**2))
                heading_des = math.atan2((y_des-self.y), (x_des -self.x))


                # Define the propotional gains of the controller
                K_linear = 0.5
                K_angular = 4

                # Define the P-controller
                velocity_message.linear.x = distance*K_linear
                heading_error = heading_des - self.z
                velocity_message.angular.z = heading_error*K_angular

                rospy.loginfo("Turtlesim moving to desination. Distance remaining %f"%distance)
                rospy.loginfo("Turning to the desired heading of %f"%heading_des)
                self.velocity_publisher.publish(velocity_message)
                self.loop_rate.sleep()

                if (distance < 0.01):
                    break
            except KeyboardInterrupt:
                pass
            
        velocity_message.linear.x = 0
        velocity_message.angular.z = 0
        self.velocity_publisher.publish(velocity_message)






if __name__ == "__main__":
    
    try:
        # Initialize the node
        rospy.init_node("robot_motion_node", anonymous=True)
        m = move()
        #pose_topic = '/turtle1/pose'
        #pose_subscriber = rospy.Subscriber(pose_topic, Pose, m.pose_callback)
        #rospy.sleep(2)
        #m.move_straight(1, 4)
        #m.move_angular(1, 270)
        #m.go_destination(9, 1)

        for i in range (30):
            m.move_straight(4, 3)
            m.move_angular(4, 90)
        rospy.spin()
        
        
    except KeyboardInterrupt:
        pass


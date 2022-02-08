#!/usr/bin/env python3

# This is a server node for the add two integer service
# Import all necesay packages including the service file, request adn response files
from homework.srv import  AddTwoInts
from homework.srv import AddTwoIntsRequest
from homework.srv import AddTwoIntsResponse
import time
import rospy

# define the callback functin
def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    time.sleep(5)
    sum_response = AddTwoIntsResponse(req.a + req.b)
    return sum_response


# define the server function
def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    serv = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print('Ready to add two integerts')
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('add_two_ints_server')
    add_two_ints_server()
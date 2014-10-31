#!/usr/bin/env python

from OliviaROS.srv import *
import rospy

def handle_add_two_ints(req):
    if req.arm:
        print "arming ..."
    else:
        print "disarming ..."

    return True

def add_two_ints_server():
    rospy.init_node('set_arm')
    s = rospy.Service('set_arm', setarm, handle_add_two_ints)
    print "Ready to ARM."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
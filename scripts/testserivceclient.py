#!/usr/bin/env python

import sys
import rospy
from OliviaROS.srv import *

def add_two_ints_client():
    rospy.wait_for_service('set_arm')
    try:
        set_arm = rospy.ServiceProxy('set_arm', setarm)
        resp1 = set_arm(True)
        return resp1.sucessful
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print "Trying to arm {0}".format(add_two_ints_client())
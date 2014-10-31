#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from OliviaROS.msg import RAW_GPS

def talker():
    pub = rospy.Publisher('RAW_GPS', RAW_GPS, queue_size=10)
    rospy.init_node('DRONE_DATA', anonymous=True)
    r = rospy.Rate(30) # 10hz
    while not rospy.is_shutdown():
        str = "hello world %s"%rospy.get_time()
        GPS = RAW_GPS()
        GPS.alt = 0
        rospy.loginfo(GPS)
        pub.publish(GPS)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
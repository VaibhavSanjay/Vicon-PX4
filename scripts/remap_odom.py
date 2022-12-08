#!/usr/bin/env python
import rospy

from nav_msgs.msg import Odometry

def odometryCb(msg):
    print msg.pose.pose

if __name__ == "__main__":
    rospy.init_node('odometry', anonymous=True) #make node 
    rospy.Subscriber('/raas_drone/odom',Odometry,odometryCb)
    rospy.spin()

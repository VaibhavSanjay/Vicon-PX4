#!/usr/bin/env python
import rospy

from nav_msgs.msg import Odometry

pub = rospy.Publisher("/mavros/odometry/out", Odometry, queue_size=10)

def callback(msg):
	global pub
	
	msg.header.frame_id = "world"
	msg.child_frame_id = "base_link"
	pub.publish(msg)
    

if __name__ == "__main__":
    rospy.init_node('odometry', anonymous=True) #make node
    model = rospy.get_param("~model")

    rospy.Subscriber('/%s/odom' % model, Odometry, callback)
    rospy.spin()

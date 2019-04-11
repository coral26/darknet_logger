#! /usr/bin/env python

import rospy
import rosbag
import datetime
from darknet_ros_msgs.msg import BoundingBoxes

def callback(data):
	#print data
	#print
	bag.write('/udp/darknet_ros/bounding_boxes',data)

def darknet_logger():
	rospy.init_node('darknet_ros_logger', anonymous=False)
	global bag

	timestamp = datetime.datetime.utcfromtimestamp(rospy.Time.now().to_time()).isoformat()
	bag = rosbag.Bag('nodes/darknet_ros_'+('-'.join(timestamp.split(':')))+'.bag', 'w', rosbag.Compression.BZ2)

	while not rospy.is_shutdown():
		rospy.Subscriber('/udp/darknet_ros/bounding_boxes',BoundingBoxes,callback)

	bag.close()




if __name__=='__main__':
	try:
		darknet_logger()
	except rospy.ROSInterruptException:
		pass



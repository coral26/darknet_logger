#! /usr/bin/env python

import rospy
import rosbag
import datetime
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes

def callback_BB(data):
	#print data
	#print
	bag.write('/darknet_ros/bounding_boxes',data)

def callback_DI(data):
	#print data
	#print
	bag.write('/darknet_ros/detection_image',data)

def darknet_logger():
	rospy.init_node('darknet_logger', anonymous=False)
	global bag

	timestamp = datetime.datetime.utcfromtimestamp(rospy.Time.now().to_time()).isoformat()
	#bag = rosbag.Bag('nodes/darknet_ros_'+('-'.join(timestamp.split(':')))+'.bag', 'w')
        bag = rosbag.Bag('/media/exfat/jetson2/nodes/darknet_ros_'+('-'.join(timestamp.split(':')))+'.bag', 'w')

	rospy.Subscriber('/darknet_ros/bounding_boxes',BoundingBoxes,callback_BB)
        rospy.Subscriber('/darknet_ros/detection_image',Image,callback_DI)
	rospy.spin()

	bag.close()




if __name__=='__main__':
	try:
		darknet_logger()
	except rospy.ROSInterruptException:
		pass



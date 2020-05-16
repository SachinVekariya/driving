#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from driving.msg import Driving_msg
import time

t = Driving_msg()

def keys_cb(msg,pub):
	if(msg.buttons[9]==1):
		t.reset=1
		t.twist.linear.x=0
		t.twist.angular.z=0
		time.sleep(1)
	
		
	else:
		t.reset=0
		if msg.buttons[4] == 1:
			t.twist.linear.x=msg.axes[1]*5
			t.twist.angular.z=msg.axes[2]*5
			t.m1=0
			t.m2=0
	
		elif(msg.axes[1]!=0):
			t.twist.linear.x=msg.axes[1]*10
			t.twist.angular.z=0
			t.m1=0
			t.m2=0
		elif(msg.axes[2]!=0):
			t.twist.linear.x=0
			t.twist.angular.z=msg.axes[2]*10
			t.m1=0
			t.m2=0
		elif(msg.buttons[0]==1):
			t.m1=255
			t.m2=0
			t.twist.linear.x=0
			t.twist.angular.z=0
		elif(msg.buttons[2]==1):
			t.m1=-255
			t.m2=0
			t.twist.linear.x=0
			t.twist.angular.z=0
		elif(msg.buttons[1]==1):
			t.m1=0
			t.m2=255
			t.twist.linear.x=0
			t.twist.angular.z=0
		elif(msg.buttons[3]==1):
			t.m1=0
			t.m2=-255
			t.twist.linear.x=0
			t.twist.angular.z=0
		else:				
			t.twist.linear.x=0
			t.twist.angular.z=0
			t.m1=0
			t.m2=0
			t.twist.linear.x=0
			t.twist.angular.z=0


	print(t)
	
	pub.publish(t)

if __name__ == '__main__':
	rospy.init_node('JOYstick')
	pub = rospy.Publisher('/cmd_vel', Driving_msg, queue_size=10)
	rospy.Subscriber('joy',Joy,keys_cb,pub)
	rospy.spin()


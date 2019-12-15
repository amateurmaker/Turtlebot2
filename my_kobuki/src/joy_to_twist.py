#! /usr/bin/env python 

import rospy 
from std_msgs.msg import String 
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import Joy 
#from kobuki_msgs.msg import MotorPower 

def callback(data):
    global g_last_twist
    #global power
    g_last_twist.linear.x = 0.5*data.axes[1]
    g_last_twist.angular.z = data.axes[3]
    twist_pub.publish(g_last_twist)
    #motor_power_pub.publish(power.ON)

if __name__=='__main__':
    rospy.init_node('keys_to_twist')
    twist_pub = rospy.Publisher("mobile_base/commands/velocity", Twist, queue_size=10)
    #motor_power_pub = rospy.Publisher("mobile_base/commands/motor_power", MotorPower, queue_size = 1)
    rospy.Subscriber("joy", Joy, callback)

    rate = rospy.Rate(10)
    g_last_twist = Twist()
    while not rospy.is_shutdown():
        twist_pub.publish(g_last_twist)
        #motor_power_pub.publish(power.ON)
        rate.sleep()



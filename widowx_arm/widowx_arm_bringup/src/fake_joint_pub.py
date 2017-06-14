#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

rospy.init_node("fake_joint_pub")
p = rospy.Publisher('joint_states', JointState, queue_size=5)

msg = JointState()
msg.name = ["gripper_prismatic_joint_1"]
msg.position = [0.0 for name in msg.name]
msg.velocity = [0.0 for name in msg.name]

msg2 = JointState()
msg2.name = ["gripper_revolute_joint"]
msg2.position = [0.0 for name in msg.name]
msg2.velocity = [0.0 for name in msg.name]

while not rospy.is_shutdown():
    #msg.header.stamp = rospy.Time.now()
    #p.publish(msg)
    #msg2.header.stamp = rospy.Time.now()
    #p.publish(msg2)
    rospy.sleep(0.05)


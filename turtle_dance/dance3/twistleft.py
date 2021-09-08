#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
from random import randint

# define state TwistLeft
class TwistLeft(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_circle','do_line'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is twisting left')
 	time.sleep(2)
  	value = randint(1, 10)
        rospy.loginfo('Value is %s', value)
        if (value > 5):
            return 'do_circle'
        else:
            return 'do_line'


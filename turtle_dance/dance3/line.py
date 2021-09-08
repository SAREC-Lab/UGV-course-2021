#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist

# define state line
class Line(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_stop'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is going straight')
	time.sleep(2)
        return 'do_stop'

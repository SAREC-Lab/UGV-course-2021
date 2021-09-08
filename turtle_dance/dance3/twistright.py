#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist

# define state TwistRight
class TwistRight(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_twist_left'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is twisting right')
 	time.sleep(2)       
        return 'do_twist_left'

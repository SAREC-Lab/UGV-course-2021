#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
from dance4.twistright import TwistRight
from dance4.twistleft import TwistLeft
from dance4.circle import Circle
from dance4.line import Line

# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle has stopped')
	time.sleep(1)
        return 'do_exit'

# main
def main():

    rospy.init_node('smach_turtle_dance')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('TwistRight', TwistRight(), 
                               transitions={'do_twist_left':'TwistLeft'})
        smach.StateMachine.add('TwistLeft', TwistLeft(), 
                                transitions={'do_circle':'Circle','do_line':'Line'})
        smach.StateMachine.add('Circle', Circle(), 
                               transitions={'do_stop':'Stop'})
        smach.StateMachine.add('Line', Line(), 
                               transitions={'do_stop':'Stop'})
        smach.StateMachine.add('Stop', Stop(), 
                               transitions={'do_exit':'do_exit'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()

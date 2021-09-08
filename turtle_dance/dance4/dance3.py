#!/usr/bin/env python
# Simple dance with example of a conditional transition

import rospy
import smach
import time
import twistright
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

# define state circle
class Circle(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_stop'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is turning in a circle')
	time.sleep(2)
        return 'do_stop'

# define state line
class Line(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_stop'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is going straight')
	time.sleep(2)
        return 'do_stop'

# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle has stopped')
	time.sleep(2)
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

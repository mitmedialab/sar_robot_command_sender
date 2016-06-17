#!/usr/bin/env python

# Jacqueline Kory Westlund
# May 2016
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Personal Robots Group
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import rospy
from sar_robot_command_msgs.msg import RobotCommand
from std_msgs.msg import Header
import argparse
import json

# SAR Robot Command Sender uses ROS to send generic robot command messages to
# a SAR robot via the /robot_command topic, and possible, the robot command
# translation node
def robot_command_sender():
    """ Use ROS to send messages to a SAR robot """
    # parse python arguments 
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Send a message to a SAR robot. Must have roscore ' 
            + 'running for message to be sent.')
    parser.add_argument('-d', '--do', dest='do', action='append', nargs='+',
            help='tell robot to speak and/or do actions/behaviors')
    parser.add_argument('-s', '--sleep', choices=['sleep','s','wakeup','w'],
            type=str, dest='sleep', help='tell robot to sleep or to wake up')
    parser.add_argument('-i', '--id', dest='id', action='append', nargs='+',
            help='provide id string alongside a command')
 
    args = parser.parse_args()
    print(args)
    
    # now build a message based on the command:
    # open ros up here, then run through the below and send all

    # start ROS node
    pub = rospy.Publisher('robot_command', RobotCommand, queue_size=10)
    rospy.init_node('robot_command_sender', anonymous=True)
    r = rospy.Rate(10) # spin at 10 Hz
    r.sleep() # sleep to wait for subscribers

    # start building message
    msg = RobotCommand()
    msg.header = Header()
    msg.header.stamp = rospy.Time.now()

    # send sleep or wakeup command
    if args.sleep:
        # build message
        print (args.sleep)
        if args.sleep == 'sleep' or args.sleep == 's':
            msg.command = RobotCommand.SLEEP 
        else:
           msg.command = RobotCommand.WAKEUP
        # check whether we were given an ID or not 
        if args.id:
            msg.id = args.id[0]

    # send robot say/do command
    elif args.do:
        # build message
        msg.command = RobotCommand.DO
        # assume we were given the necessary properties in the right
        # format and just pass them along
        msg.properties = args.do[0]
        # check whether we were given an ID or not 
        if args.id:
            msg.id = args.id[0]

    # don't send message unless we got something to send
    else:
        return

    # send message
    pub.publish(msg)
    rospy.loginfo(msg)
    r.sleep()

        
if __name__ == '__main__':
    try:
        robot_command_sender()
    except rospy.ROSInterruptException:
        print('ROSnode shutdown')

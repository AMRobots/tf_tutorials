#!/usr/bin/env python

import rospy

import tf   #TransForm package
import turtlesim.msg    #Message Format:
                        #float32 x
                        #float32 y
                        #float32 theta
                        #float32 linear_velocity
                        # float32 angular_velocity

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()      #create TransformBroadcaster instance

    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")       #TransForm world frame to turtlename frame

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')    #create node

    turtlename = rospy.get_param('~turtle')     #get turtle param

    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)                #create Subscriber
                                                #function handler: handle_turtle_pose
                                                #addtional argument: turtlename

    rospy.spin()                                #simply keeps python from exiting
                                                #until this node is stopped
                                                #it create new thread, so don't affect Subscriber

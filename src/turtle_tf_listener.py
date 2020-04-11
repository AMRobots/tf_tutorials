#!/usr/bin/env python
# import roslib
# roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener')   #create node

    listener = tf.TransformListener()   #create TransformListener instance

    rospy.wait_for_service('spawn')     #Blocks until service is available
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn) #Create a handle to a ROS service
                                                               #for invoking calls

    spawner(4, 2, 0, 'turtle2')   # create 2th turtle

    #create Publisher
    turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1)

    rate = rospy.Rate(10.0) #Publish rate =10 Hz

    while not rospy.is_shutdown():
        try:
            #get us the latest available transform from turtle1 to turtle2 frame
            (trans,rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()    #sleep to keep rate =10hz

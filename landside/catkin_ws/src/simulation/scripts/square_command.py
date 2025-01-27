#!/usr/bin/env python3

import rospy
from custom_msgs.msg import ThrusterSpeeds

if __name__ == "__main__":
    pub = rospy.Publisher("/offboard/thruster_speeds", ThrusterSpeeds, queue_size=10)
    rospy.init_node("sim_move_square")

    # Initialize direction vectors
    forwards = (127, 127, 127, 127, 0, 0, 0, 0)
    backwards = (-127, -127, -127, -127, 0, 0, 0, 0)
    right = (-127, 127, 127, -127, 0, 0, 0, 0)  # top view
    left = (127, -127, -127, 127, 0, 0, 0, 0)
    dirs = (forwards, right, backwards, left)
    ct = 0

    start = rospy.Time.now()

    while not rospy.is_shutdown():
        data = ThrusterSpeeds()
        if (rospy.Time.now() - start).to_sec() > 5:
            ct = (ct + 1) % 4
            start = rospy.Time.now()
        data.speeds = dirs[ct]
        pub.publish(data)

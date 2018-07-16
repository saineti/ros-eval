#! /usr/bin/env python
  
import fetch_api
import rospy
import time

def wait_for_time():
    """Wait for simulated time to begin.
    """
    while rospy.Time().now().to_sec() == 0:
        pass


def main():
    rospy.init_node('erase_whiteboard_demo')
    wait_for_time()
    argv = rospy.myargv()
    ERASE_POSES = [[-0.239, -0.433, 1.401, 0.758, -2.997, 0.565, 1.742],
                   [-0.530, -0.423, 1.438, 0.714, -2.983, 0.266, 1.689],
                   [-0.251, -0.400, 1.469, 0.755, -2.993, 0.576, 1.667],
                   [-0.556, -0.395, 1.437, 0.726, -2.982, 0.181, 1.690]]

    torso = fetch_api.Torso()
    torso.set_height(0.4)

    display = fetch_api.Display()
    display.display_msg("Hello! I am going to erase the whiteboard for you!")
    time.sleep(7)

    gripper = fetch_api.Gripper()
    gripper.close()
    time.sleep(2)

    arm = fetch_api.Arm()
    torso.set_height(0.0)
    for vals in ERASE_POSES:
        arm.move_to_joints(fetch_api.ArmJoints.from_list(vals))

    time.sleep(5)
    display.display_msg("All done!")
    time.sleep(2)

if __name__ == '__main__':
    main()


#! /usr/bin/env python
  
import fetch_api
import rospy
import time

def print_usage():
    print 'Moves the torso to a certain height between [0.0, 0.4]'
    print 'Usage: rosrun applications torso_demo.py 0.4'


def wait_for_time():
    """Wait for simulated time to begin.
    """
    while rospy.Time().now().to_sec() == 0:
        pass


def main():
    rospy.init_node('raising_torso_demo')
    wait_for_time()
    argv = rospy.myargv()

    torso = fetch_api.Torso()
    blinky = fetch_api.Blinky()


    blinky.display_msg("I\'m going to raise my torso now!")
    time.sleep(2)
    torso.set_height(0.4)
    choices = ["Stop!"]
    blinky.ask_mc("Press \'Stop!\' whenever I am tall enough for you!", choices)
    while not blinky.is_done() and not torso.is_done(): 
        time.sleep(0.2)
    
    item = blinky.get_result()
    if item == "Stop!":
        torso.cancel()
        blinky.display_msg("Perfect!")
    else:
        blinky.display_msg("I only get this tall!")

    time.sleep(2)


if __name__ == '__main__':
    main()


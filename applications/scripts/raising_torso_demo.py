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
    rospy.init_node('raising_torso_demo')
    wait_for_time()
    
    torso = fetch_api.Torso()
    display = fetch_api.Display()

    display.display_msg("I\'m going to raise my torso now!")
    time.sleep(2)
    torso.set_height(0.4)
    choices = ["Stop!"]
    display.ask_mc("Press \'Stop!\' whenever I am tall enough for you!", choices)
    while not display.is_done() and not torso.is_done(): 
        time.sleep(0.2)
    
    if display.is_done():
        torso.cancel()
        display.display_msg("Perfect!")
    else:
        display.display_msg("I only get this tall!")
    time.sleep(2)
    display.cancel()

if __name__ == '__main__':
    main()


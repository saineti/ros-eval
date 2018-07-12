#!/usr/bin/env python
  
import actionlib
import actionlib_msgs
import rospy
import blinky.msg

ACTION_SERVER = 'blinky'

class Display(object):
    """Blinky controls the Blinky face.
    """
    def __init__(self):
        self._client = actionlib.SimpleActionClient(
            ACTION_SERVER, blinky.msg.FaceAction)
        self._client.wait_for_server(rospy.Duration(10))

    def ask_mc(self, question, choices):
        """ Asks a multiple choice question.

        Args:
            question: The question to ask.
            choices: The possible choices for the question.
        """
        goal = blinky.msg.FaceGoal()
        goal.display_type = 'askMultipleChoice' 
        goal.question = question
        goal.choices = choices
        self._client.send_goal(goal)

    def display_msg(self, message):
        goal = blinky.msg.FaceGoal()
        goal.display_type = 'displayMessage' 
        goal.h1_text = message
        goal.h2_text = ''

        self._client.send_goal(goal)

    def cancel(self):
        goal = blinky.msg.FaceGoal()
        goal.display_type = 'default' 
        self._client.send_goal(goal)

    def get_result(self):
        return self._client.get_result()

    def is_done(self):
        state = self._client.get_state()
        if state == actionlib_msgs.msg.GoalStatus.PREEMPTED or \
            state == actionlib_msgs.msg.GoalStatus.RECALLED or \
            state == actionlib_msgs.msg.GoalStatus.REJECTED or \
            state == actionlib_msgs.msg.GoalStatus.ABORTED or \
            state == actionlib_msgs.msg.GoalStatus.SUCCEEDED or \
            state == actionlib_msgs.msg.GoalStatus.LOST: 
          return True
        
        return False

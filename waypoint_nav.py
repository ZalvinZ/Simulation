#!/usr/bin/env python3
# Copyright 2021 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import sys
import tty
import termios

def get_key():
    # Function to get a single key press from the user
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_user_input():
    # Function to get user input for waypoints
    x = float(input("Enter x-coordinate for waypoint: "))
    y = float(input("Enter y-coordinate for waypoint: "))
    return x, y

def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 3.45
    initial_pose.pose.position.y = 2.15
    initial_pose.pose.orientation.z = 1.0
    initial_pose.pose.orientation.w = 0.0
    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()

    # Get user input for waypoints. User can put in the amount of waay points and the x and y coordinates for each waypoint.
    goal_poses = []
    num_waypoints = int(input("Enter the number of waypoints: "))
    for _ in range(num_waypoints):
        x, y = get_user_input()
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = x
        goal_pose.pose.position.y = y
        goal_poses.append(goal_pose)

    nav_start = navigator.get_clock().now()
    navigator.followWaypoints(goal_poses)

    while not navigator.isTaskComplete():
        ch = get_key()
        if ch.lower() == 's':
            print("Stopping the robot!")
            navigator.cancelTask()
            break  # Exit the loop when 's' is pressed

        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print(
                'Executing current waypoint: '
                + str(feedback.current_waypoint + 1)
                + '/'
                + str(len(goal_poses))
            )
            now = navigator.get_clock().now()

            if now - nav_start > Duration(seconds=600.0):
                navigator.cancelTask()

            if now - nav_start > Duration(seconds=35.0):
                goal_pose4 = PoseStamped()
                goal_pose4.header.frame_id = 'map'
                goal_pose4.header.stamp = now.to_msg()
                goal_pose4.pose.position.x = -5.0
                goal_pose4.pose.position.y = -4.75
                goal_pose4.pose.orientation.w = 0.707
                goal_pose4.pose.orientation.z = 0.707
                goal_poses = [goal_pose4]
                nav_start = now
                navigator.followWaypoints(goal_poses)

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)

if __name__ == '__main__':
    main()

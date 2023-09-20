#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="udemy_ros2_pkg",
            executable="rpm_pub.py",
            name="rpm_pub",
        ),
        Node(
            package="udemy_ros2_pkg",
            executable="speed_pub.py",
            name="speed_pub",
            parameters=[
                {"wheel_radius":100.0}
            ]
        ),
        ExecuteProcess(
            cmd=['ros2', 'topic', 'echo', '/speed'],
            output='screen'
        )
    ])
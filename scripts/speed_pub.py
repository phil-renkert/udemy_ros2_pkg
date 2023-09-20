#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SpeedPub(Node):
    def __init__(self):
        super().__init__("speed_pub_node")

        self.sub = self.create_subscription(Float32, "rpm", self.rpm_subscription, 10)
        self.pub = self.create_publisher(Float32, "speed", 10)
        self.declare_parameter("wheel_radius", value=0.125)

        print(self.get_parameter("wheel_radius").get_parameter_value())

    def rpm_subscription(self, msg):
        rpm = msg.data
        wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        speed = rpm * wheel_radius

        speed_msg = Float32()
        speed_msg.data = speed
        self.pub.publish(speed_msg)

def main():
    rclpy.init()

    node = SpeedPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()

if __name__ == "__main__":
    main()
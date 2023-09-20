#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class PubNode(Node):
    def __init__(self):
        super().__init__("rpm_pub_node")

        self.pub = self.create_publisher(Float32, "rpm", 10)
        self.timer = self.create_timer(1, callback=self.publish_rpm)

    def publish_rpm(self):
        msg = Float32()
        msg.data = 100.0

        self.pub.publish(msg)

def main():
    rclpy.init()

    pub_node = PubNode()

    try:
        rclpy.spin(pub_node)
    except KeyboardInterrupt:
        pub_node.destroy_node()

if __name__ == "__main__":
    main()
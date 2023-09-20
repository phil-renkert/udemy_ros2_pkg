#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloWorldSubscriber(Node):
	def __init__(self):
		super().__init__("hello_world_subscriber_node")

		self.sub = self.create_subscription(String, "hello_world", self.subscriber_callback, 10)
	
	def subscriber_callback(self, msg : String):
		print("Received: " + msg.data)


def main(args=None):
	rclpy.init()

	my_sub = HelloWorldSubscriber()

	try:
		rclpy.spin(my_sub)
	except KeyboardInterrupt:
		my_sub.destroy_node()


if __name__ == "__main__":
	main()


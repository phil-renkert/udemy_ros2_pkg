#!/usr/bin/env python3
import rclpy
import cv2

from rclpy.node import Node
from udemy_ros2_pkg.srv import Image
from cv_bridge import CvBridge

class ImageClient(Node):
    def __init__(self):
        super().__init__('odd_even_service_client_node')
        self.client = self.create_client(Image, 'image_service')
        self.req = Image.Request()

    def send_request(self, num):
        self.req.angle = float(num)
        self.client.wait_for_service()
        self.future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        self.result = self.future.result()
        return self.result
    
def main(args=None):
    rclpy.init()
    client_node = ImageClient()
    print("Image Client Running...")

    try:
        user_input = input("Enter an Integer: ")
        res = client_node.send_request(user_input)
        print("Server returned the image!")
        img = CvBridge().imgmsg_to_cv2(res.image)

        cv2.imshow("Image Window", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except KeyboardInterrupt:
        print("Terminating Node...")
        client_node.destroy_node()

if __name__ == "__main__":
    main()
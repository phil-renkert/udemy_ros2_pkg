#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from pathlib import Path

from udemy_ros2_pkg.srv import Image


class ImageServer(Node):
    def __init__(self):
        super().__init__('image_server_node')
        self.srv = self.create_service(Image, 'image_service', self.return_image)
        self.available_angles = [-30, -15, 0, 15, 30]
    
    def return_image(self, request, response):
        print("Request was received")

        angle_deltas = [abs(request.angle - angle) for angle in self.available_angles]
        angle_index = angle_deltas.index(min(angle_deltas))
        angle = self.available_angles[angle_index]

        img_name = str(angle)+".png"
        file_path = Path(__file__)
        file_parts = file_path.parts
        home_dir = Path(*file_parts[0:file_parts.index("install")])
        image_dir = home_dir/"src"/"udemy_ros2_pkg"/"images"
        image_path = image_dir / img_name

        img = cv2.imread(str(image_path))
        img_msg = CvBridge().cv2_to_imgmsg(img)
        response.image = img_msg

        return response
    
def main(args=None):
    rclpy.init()
    server_node = ImageServer()
    print("Image Service Server Running...")

    try:
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        print("Terminating Node...")
        server_node.destroy_node()

if __name__ == "__main__":
    main()
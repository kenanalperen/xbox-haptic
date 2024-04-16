#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped
from std_msgs.msg import Float64 
from sensor_msgs.msg import JoyFeedback  # Add import for JoyFeedback message type

class ForceReaderNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("force_reader") # MODIFY NAME

        self.subscription = self.create_subscription(
            WrenchStamped,
            'moca_red/ATI45_ft_handler/wrench',  # Change '/wrench_topic' to your desired topic name
            self.wrench_callback,
            10  # QoS profile depth
        )
        
        # Publisher for z-force data
        self.publisher_z_force = self.create_publisher(Float64, '/z_force', 10)

        # Publisher for JoyFeedback message
        self.publisher_joy_feedback = self.create_publisher(JoyFeedback, '/joy/set_feedback', 10)

    def wrench_callback(self, msg):
         # Extract z-force data
        z_force = msg.wrench.force.z

        # Publish z-force data
        z_force_msg = Float64()
        z_force_msg.data = z_force
        self.publisher_z_force.publish(z_force_msg)

        # Calculate intensity value based on z-force
        intensity = 0.5 if z_force > 25 else 0.0

        # Publish JoyFeedback message
        joy_feedback_msg = JoyFeedback()
        joy_feedback_msg.type = 1
        joy_feedback_msg.id = 0
        joy_feedback_msg.intensity = intensity
        self.publisher_joy_feedback.publish(joy_feedback_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ForceReaderNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

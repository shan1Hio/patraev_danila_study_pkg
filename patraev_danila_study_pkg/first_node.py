"""Timer"""

import rclpy
import time
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)                  
    node = Node('Time_printer')              
    node.get_logger().info("Timer has started")
    def timer_callback():
        current_time = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        node.get_logger().info(f"Current time: {time_str}")
    timer = node.create_timer(5.0, timer_callback)
    rclpy.spin(node)                        
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
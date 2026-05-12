#!/usr/bin/env python3
import rclpy                       
from rclpy.node import Node         
from std_msgs.msg import Int32    

class overflow_l(Node):

    def __init__(self):
        super().__init__('overflow_l')
        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.callback,
            10)

        self.get_logger().info("Узел overflow_l запущен и слушает топик!")

   
    def callback(self, msg):
        self.get_logger().info(f"[WARN] [overflow_l]:!!! OVERFLOW !!! Resulting number is {msg.data}")

def main():
    rclpy.init()                    
    node = overflow_l()            
    try:
        rclpy.spin(node)           
    except KeyboardInterrupt:
        pass                        
    finally:
        node.destroy_node()         
        rclpy.shutdown()            

if __name__ == '__main__':
    main()
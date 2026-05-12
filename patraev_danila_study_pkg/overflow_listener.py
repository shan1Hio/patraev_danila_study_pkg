# #!/usr/bin/env python3
# import rclpy                       
# from rclpy.node import Node         
# from std_msgs.msg import Int32    

# class overflow_l(Node):

#     def __init__(self):
#         super().__init__('overflow_l')
#         self.subscription = self.create_subscription(
#             Int32,
#             'overflow',
#             self.callback,
#             10)

#         self.get_logger().info("Узел overflow_l запущен и слушает топик!")

   
#     def callback(self, msg):
#         self.get_logger().info(f"[WARN] [overflow_l]:!!! OVERFLOW !!! Resulting number is {msg.data}")

# def main():
#     rclpy.init()                    
#     node = overflow_l()            
#     try:
#         rclpy.spin(node)           
#     except KeyboardInterrupt:
#         pass                        
#     finally:
#         node.destroy_node()         
#         rclpy.shutdown()            

# if __name__ == '__main__':
#     main()

#!/usr/bin/env python3
import rclpy                        
from rclpy.node import Node        
from std_msgs.msg import Int32    

class overflow_l(Node):

    def __init__(self):
        super().__init__('overflow_l')

        self.declare_parameter('overflow_threshold', 80) 
        self.declare_parameter('topic_name_2', 'overflow')
        self.declare_parameter('node_name_2', 'overflow_l')

        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic_2 = self.get_parameter('topic_name_2').value
        self.node_2 = self.get_parameter('node_name_2').value

        self.subscription = self.create_subscription(
            Int32,
            self.topic_2,
            self.callback,
            10)

        self.get_logger().info(f'Узел {self.node_2} запущен и слушает топик!')

   
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
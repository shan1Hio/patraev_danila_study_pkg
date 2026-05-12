# import rclpy                        
# from rclpy.node import Node        
# from std_msgs.msg import Int32     

# class even_pub(Node):

#     def __init__(self):
#         super().__init__('even_pub')

#         self.declare_parameter('publish_frequency', 10.0)   
#         self.declare_parameter('overflow_threshold', 100)
#         self.declare_parameter('topic_name', '/even_numbers')

#         self.freq = self.get_parameter('publish_frequency').value
#         self.threshold = self.get_parameter('overflow_threshold').value
#         self.topic = self.get_parameter('topic_name').value

#         self.publisher = self.create_publisher(Int32, self.topic, 10)
#         self.timer = self.create_timer(1.0 / self.freq, self.timer_callback)

#         self.publisher_over = self.create_publisher(Int32,'overflow', 10)       
#         self.counter = 0
#         self.get_logger().info("Узел even_pub запущен!")
    
#     def timer_callback(self):
#         msg = Int32()                      
#         msg.data = self.counter
#         self.publisher.publish(msg)         
#         self.get_logger().info(f'Number equal {msg.data}')  
#         if self.counter >= 100:
#             self.publisher_over.publish(msg)
#             self.counter = 0 
#         else:
#             self.counter += 10
        
    
# def main():
#     rclpy.init()                    

#     node = even_pub()                 

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

class even_pub(Node):

    def __init__(self):
        super().__init__('even_pub')

        self.declare_parameter('publish_frequency', 8.0)   
        self.declare_parameter('overflow_threshold', 80) 
        self.declare_parameter('topic_name_1', 'even_numbers')
        self.declare_parameter('topic_name_2', 'overflow')
        self.declare_parameter('node_name_1', 'even_pub')

        self.freq = self.get_parameter('publish_frequency').value
        self.threshold = self.get_parameter('overflow_threshold').value
        self.topic_1 = self.get_parameter('topic_name_1').value
        self.topic_2 = self.get_parameter('topic_name_2').value
        self.node_1 = self.get_parameter('node_name_1').value

        self.publisher = self.create_publisher(Int32,self.topic_1, 10)
        self.publisher_over = self.create_publisher(Int32,self.topic_2, 10)   
        self.timer = self.create_timer(1.0 / self.freq, self.timer_callback)
        self.counter = 0
        self.get_logger().info(f'Узел {self.node_1} запущен!')
    
    def timer_callback(self):
        msg = Int32()                      
        msg.data = self.counter
        self.publisher.publish(msg)         
        self.get_logger().info(f'Number equal {msg.data}')  
        if self.counter >= self.threshold:
            self.publisher_over.publish(msg)
            self.counter = 0 
        else:
            self.counter += 10
        
def main():
    rclpy.init()                    
    node = even_pub()                 

    try:
        rclpy.spin(node)            
    except KeyboardInterrupt:
        pass                        
    finally:
        node.destroy_node()         
        rclpy.shutdown()            


if __name__ == '__main__':
    main()
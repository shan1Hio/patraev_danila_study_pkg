"""Timer"""

import rclpy
import time
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)                   # инициализация ROS 2
    node = Node('Time_printer')               # создаём узел с именем hello_node
    node.get_logger().info("Timer has started")
    def timer_callback():
        current_time = time.localtime()
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
        node.get_logger().info(f"Current time: {time_str}")
    timer = node.create_timer(5.0, timer_callback)
    rclpy.spin(node)                        # запускаем цикл обработки
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
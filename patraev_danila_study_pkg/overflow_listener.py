#!/usr/bin/env python3
import rclpy                        # главная библиотека ROS 2
from rclpy.node import Node         # от неё наследуемся
from std_msgs.msg import Int32    # тип сообщения — строка

class overflow_l(Node):

    def __init__(self):
        # Даём узлу имя "listener"
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
    rclpy.init()                    # стартуем ROS 2
    node = overflow_l()               # создаём наш узел
    try:
        rclpy.spin(node)            # крутимся и ждём сообщений
    except KeyboardInterrupt:
        pass                        # Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2

if __name__ == '__main__':
    main()
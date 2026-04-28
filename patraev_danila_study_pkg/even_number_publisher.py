
#!/usr/bin/env python3
import rclpy                        
from rclpy.node import Node        
from std_msgs.msg import Int32     

# ────────────────────────────────────────────────
# 1. Создаём класс — это и есть наш узел
# ────────────────────────────────────────────────
class even_pub(Node):

    def __init__(self):
        super().__init__('even_pub')
        self.publisher = self.create_publisher(Int32,'even_numbers', 10)
        self.publisher_over = self.create_publisher(Int32,'overflow', 10)
        timer_period = 1.0          # 1 секунда = 1 Гц
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
        self.get_logger().info("Узел even_pub запущен!")
    

    # ────────────────────────────────────────────────
    # 2. Эта функция будет вызываться каждую секунду
    # ────────────────────────────────────────────────
    def timer_callback(self):
        msg = Int32()                      # создаём пустое сообщение
        msg.data = self.counter
        self.publisher.publish(msg)         # отправляем сообщение в топик
        self.get_logger().info(f'Number equal {msg.data}')  
        if self.counter >= 100:
            self.publisher_over.publish(msg)
            self.counter = 0 
        else:
            self.counter += 10
        
        



# ────────────────────────────────────────────────
# 3. Главная функция — точка входа
# ────────────────────────────────────────────────
def main():
    rclpy.init()                    # начинаем работать с ROS 2

    node = even_pub()                 # создаём наш узел

    try:
        rclpy.spin(node)            # "крутимся" и ждём событий (таймеров, сообщений и т.д.)
    except KeyboardInterrupt:
        pass                        # если нажали Ctrl+C — нормально выходим
    finally:
        node.destroy_node()         # убираем узел
        rclpy.shutdown()            # завершаем ROS 2


if __name__ == '__main__':
    main()

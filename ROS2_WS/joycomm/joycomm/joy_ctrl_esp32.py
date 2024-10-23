import rclpy
import socket
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32MultiArray

class JoyCommEsp(Node):
    def __init__(self):
        super().__init__('joy_comm_esp')

        self.joy_subscriber = self.create_subscription(
            Joy,
            '/joy',
            self.joy_callback,
            10
        )

        self.motor_pub = self.create_publisher(
            Int32MultiArray,
            '/motor_signals',
            10
        )

        self.esp_ip = "192.168.204.35" #
        self.esp_port = 80 #
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.esp_ip, self.esp_port))
        self.get_logger().info('Connected to ESP32')

    def joy_callback(self, msg):
        x = msg.axes[0] 
        y = msg.axes[1] 

        r1, r2, l1, l2 = self.calculate_pwm(x, y)

        motor_data = f"{r1},{r2},{l1},{l2}\n"
        self.client_socket.sendall(motor_data.encode())

        motor_signals = Int32MultiArray(data=[r1, r2, l1, l2])
        self.motor_pub.publish(motor_signals)

    def calculate_pwm(self, x, y):
        max_pwm = 255

        L1 = min(255, max(0, (y - x) * max_pwm))
        L2 = min(255, max(0, -(y - x) * max_pwm))

        R1 = min(255, max(0, (y + x) * max_pwm))  
        R2 = min(255, max(0, -(y + x) * max_pwm))

        return int(L1), int(L2), int(R1), int(R2)

def main(args=None):
    rclpy.init(args=args)
    joy_comm_node = JoyCommEsp()
    rclpy.spin(joy_comm_node)
    joy_comm_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

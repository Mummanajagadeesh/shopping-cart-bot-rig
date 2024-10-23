import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32MultiArray

class JoyCommNode(Node):
    def __init__(self):
        super().__init__('joy_comm_node')

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

        self.get_logger().info('JoyCommNode has been started.')

    def joy_callback(self, msg):
        x = msg.axes[0] 
        y = msg.axes[1] 

        self.get_logger().info(f'Joystick input received - X: {x}, Y: {y}')

        r1, r2, l1, l2 = self.calculate_pwm(x, y)

        motor_signals = Int32MultiArray(data=[r1, r2, l1, l2])
        self.motor_pub.publish(motor_signals)

        self.get_logger().info(f'Motor signals - R1: {r1}, R2: {r2}, L1: {l1}, L2: {l2}')

    def calculate_pwm(self, x, y):
        max_pwm = 255

        left_speed = y * max_pwm - x * max_pwm
        right_speed = y * max_pwm + x * max_pwm

        L1 = min(max_pwm, max(0, left_speed))
        L2 = min(max_pwm, max(0, -left_speed))

        R1 = min(max_pwm, max(0, right_speed))
        R2 = min(max_pwm, max(0, -right_speed))

        return int(R1), int(R2), int(L1), int(L2)

def main(args=None):
    rclpy.init(args=args)
    joy_comm_node = JoyCommNode()
    rclpy.spin(joy_comm_node)
    joy_comm_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

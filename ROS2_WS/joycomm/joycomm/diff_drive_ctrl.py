import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import Int32MultiArray

class DifferentialDriveController(Node):
    def __init__(self):
        super().__init__('differential_drive_controller')
        self.subscription = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.pub = self.create_publisher(Int32MultiArray, '/wheel_pwm', 10)

        self.k_v = 1.0    
        self.k_omega = 0.5 
        self.L = 0.5    
        self.PWM_scale = 255 

    def joy_callback(self, msg):
        x = msg.axes[0]  
        y = msg.axes[1]  

        v = self.k_v * y
        omega = self.k_omega * x

        v_left = v - (self.L * omega / 2)
        v_right = v + (self.L * omega / 2)

        PWM_left = min(255, max(0, int(v_left * self.PWM_scale)))
        PWM_right = min(255, max(0, int(v_right * self.PWM_scale)))

        left_direction = 1 if v_left >= 0 else 0
        right_direction = 1 if v_right >= 0 else 0

        pwm_msg = Int32MultiArray()
        pwm_msg.data = [PWM_left, left_direction, PWM_right, right_direction]
        self.pub.publish(pwm_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DifferentialDriveController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

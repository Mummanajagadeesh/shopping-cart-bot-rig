"""line_follower_robot."""
from controller import Robot

def run_robot(robot):
    
    # get the time step of the current world.
    timestep = 32
    max_speed = 6.28 * 0.25 #angular velocity
    
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    left_ir = robot.getDevice('ir0')
    left_ir.enable(timestep)
    
    right_ir = robot.getDevice('ir1')
    right_ir.enable(timestep)
    
    
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:

        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        
        print(left_ir_value,right_ir_value)
        if left_ir_value > right_ir_value :
            print('l    ',left_ir_value-right_ir_value)
        else:
            print('r    ',right_ir_value-left_ir_value)
        
        
        left_speed = max_speed
        right_speed = max_speed
       
            
        # if (left_ir_value > right_ir_value) and ( 1 < left_ir_value < 4):
            # print('Go left')
            # left_speed = - max_speed
        # elif (right_ir_value > left_ir_value) and ( 1 < right_ir_value < 4):
            # print('Go right')
            # right_speed = - max_speed
            
            
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)

 

    # Enter here exit cleanup code.
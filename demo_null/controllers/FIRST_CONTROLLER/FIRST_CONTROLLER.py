from controller import Robot 

robot = Robot()

# Get time step of the current simulation.
timestep = int(robot.getBasicTimeStep())

# Get motor devices
motor1 = robot.getDevice('WHEEL1_MOTOR')
motor2 = robot.getDevice('WHEEL2_MOTOR')
motor3 = robot.getDevice('WHEEL3_MOTOR')
motor4 = robot.getDevice('WHEEL4_MOTOR')

# Get camera device
camera = robot.getDevice('camera')  # Ensure the camera name matches the one in your robot

# Enable the camera for image capture
camera.enable(timestep)

# Enable object recognition
recognition_sampling_period = 100  # Adjust the sampling period as needed
camera.recognitionEnable(recognition_sampling_period)

# Set the target velocity for the wheels
velocity = 5.0  # Adjust speed as needed

# Set motors to infinite position for continuous rotation
motor1.setPosition(float('inf'))
motor2.setPosition(float('inf'))
motor3.setPosition(float('inf'))
motor4.setPosition(float('inf'))

# Start moving forward
motor1.setVelocity(-velocity)
motor2.setVelocity(-velocity)
motor3.setVelocity(velocity)
motor4.setVelocity(velocity)

# Safety distance from the obstacle (adjust as necessary)
safe_distance = 0.5  # Define your safe distance threshold here

# Main loop
while robot.step(timestep) != -1:
    # Capture the recognition data
    num_objects = camera.getRecognitionNumberOfObjects()

    obstacle_detected = False  # Flag to indicate if an obstacle is detected
    closest_distance = float('inf')  # Initialize the closest distance

    # Process the recognition results
    if num_objects > 0:
        for i in range(num_objects):
            object_info = camera.getRecognitionObjects()[i]
            object_id = object_info.getId()
            object_name = object_info.getModel()  # or object_info.get_type(), etc.
            object_position = object_info.getPosition()  # Position of the object
            distance_to_obstacle = object_position[0]  # Assuming X-axis distance

            print(f"Detected object: ID={object_id}, Name={object_name}, Position={object_position}, Distance={distance_to_obstacle}")

            # Example condition: Check if the object is a specific recognized type
            if object_name == "YourObstacleType":  # Replace with the actual type or color you want to detect
                obstacle_detected = True
                # Check if the distance is less than the safe distance
                if distance_to_obstacle < safe_distance:
                    closest_distance = distance_to_obstacle
                    break  # Exit the loop if an obstacle is detected within the safe distance

    # Control logic based on obstacle detection
    if obstacle_detected and closest_distance < safe_distance:
        print("Obstacle detected within safe distance! Stopping the robot.")
        motor1.setVelocity(0)
        motor2.setVelocity(0)
        motor3.setVelocity(0)
        motor4.setVelocity(0)
    else:
        print("No obstacle detected or obstacle is at a safe distance. Continuing movement.")

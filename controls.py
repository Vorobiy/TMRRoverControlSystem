import pygame

# Function to map joystick axis values (-1 to 1) to PWM values (0 to 255)
def map_axis_to_pwm(axis_value):
    pwm_value = int((axis_value + 1) * 127.5)
    return max(0, min(255, pwm_value))  # Ensure PWM is clamped between 0 and 255

# Function to initialize the joystick and handle errors
def init_joystick():
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        raise Exception("No joystick connected!")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")
    return joystick

# Function to get joystick values and convert to PWM for the wheels
def get_wheel_pwm_values(joystick):
    left_wheel_axis = joystick.get_axis(1)  # Left joystick vertical
    right_wheel_axis = joystick.get_axis(3) # Right joystick vertical

    # Map axis to PWM values
    right_wheel_pwms = [map_axis_to_pwm(right_wheel_axis)] * 3
    left_wheel_pwms = [map_axis_to_pwm(left_wheel_axis)] * 3

    return right_wheel_pwms + left_wheel_pwms  # Combine into a single list

# Function to get joystick inputs for the arm control
def get_arm_pwm_values(joystick):
    # Buttons for wrist control (up/down & spin)
    wrist_up = joystick.get_button(3)    # Y button
    wrist_down = joystick.get_button(0)  # A button
    wrist_left = joystick.get_button(2)  # X button
    wrist_right = joystick.get_button(1) # B button

    # Shoulder control
    rotate_left = joystick.get_button(4)  # Left shoulder button
    rotate_right = joystick.get_button(5) # Right shoulder button

    # Claw control
    claw_open = joystick.get_button(6)   # Left trigger
    claw_close = joystick.get_button(7)  # Right trigger

    # Elbow control using D-Pad
    elbow_up = joystick.get_hat(0)[1] == 1   # D-Pad up
    elbow_down = joystick.get_hat(0)[1] == -1 # D-Pad down

    # Gantry control using D-Pad left/right
    gantry_up = joystick.get_hat(0)[0] == 1   # D-Pad right
    gantry_down = joystick.get_hat(0)[0] == -1 # D-Pad left

    # PWM Values Calculation
    wrist_left_pwm = map_axis_to_pwm(joystick.get_axis(2))  # Assuming axis 2 for wrist left
    wrist_right_pwm = map_axis_to_pwm(joystick.get_axis(5)) # Assuming axis 5 for wrist right

    # Determine claw spin and movement
    if 128 <= wrist_left_pwm <= 255 and 128 <= wrist_right_pwm <= 255:
        claw_pwm = 255  # Clockwise
    elif 0 <= wrist_left_pwm <= 128 and 0 <= wrist_right_pwm <= 128:
        claw_pwm = 0    # Counter-clockwise
    elif 0 <= wrist_right_pwm <= 128 and 128 <= wrist_left_pwm <= 255:
        claw_pwm = 255  # Move up
    elif 128 <= wrist_right_pwm <= 255 and 0 <= wrist_left_pwm <= 128:
        claw_pwm = 0    # Move down
    else:
        claw_pwm = 128  # Neutral

    shoulder_pwm = 255 if rotate_right else 0 if rotate_left else 128  # Shoulder rotation

    elbow_pwm = 255 if elbow_up else 0 if elbow_down else 128  # Elbow up/down
    gantry_pwm = 255 if gantry_up else 0 if gantry_down else 128  # Gantry up/down

    # Ensure values are clamped between 0 and 255
    return [
        max(0, min(255, elbow_pwm)),
        max(0, min(255, wrist_left_pwm)),  # Wrist movement (up/down)
        max(0, min(255, wrist_right_pwm)), # Wrist spin
        max(0, min(255, claw_pwm)),
        max(0, min(255, gantry_pwm)),
        max(0, min(255, shoulder_pwm))
    ]

# Function to construct the drive command packet
def construct_drive_packet(wheel_pwms):
    packet = f"D_{'_'.join(map(str, wheel_pwms))}"
    print(f"Drive packet: {packet}")
    return packet

# Function to construct the arm command packet
def construct_arm_packet(arm_pwms):
    packet = f"A_{'_'.join(map(str, arm_pwms))}"
    print(f"Arm packet: {packet}")
    return packet
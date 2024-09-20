import pygame

def map_axis_to_pwm(axis_value):
    """Map joystick axis value to PWM range (0-255)."""
    pwm_value = int((axis_value + 1) * 127.5)
    return max(0, min(255, pwm_value))

def init_joystick():
    """Initialize the joystick and return the joystick object."""
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        raise Exception("No joystick connected!")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick initialized: {joystick.get_name()}")
    return joystick

def get_wheel_pwm_values(joystick):
    """Get PWM values for the wheels based on joystick axes."""
    left_wheel_axis = joystick.get_axis(1)  # Assuming axis 1 for left wheel
    right_wheel_axis = joystick.get_axis(3)  # Assuming axis 3 for right wheel

    left_wheel_pwm = map_axis_to_pwm(left_wheel_axis)
    right_wheel_pwm = map_axis_to_pwm(right_wheel_axis)

    return [right_wheel_pwm, right_wheel_pwm, right_wheel_pwm, left_wheel_pwm, left_wheel_pwm, left_wheel_pwm]

def get_arm_pwm_values(joystick):
    """Get PWM values for the arm based on joystick buttons and D-Pad."""
    wrist_up = joystick.get_button(2)    # X button for wrist up
    wrist_down = joystick.get_button(1)  # B button for wrist down
    wrist_max = joystick.get_button(0)   # A button for max PWM on both wrists
    wrist_min = joystick.get_button(3)   # Y button for min PWM on both wrists
    rotate_left = joystick.get_button(4)  # Left shoulder button
    rotate_right = joystick.get_button(5) # Right shoulder button
    claw_open_axis = joystick.get_axis(4)   # Left trigger 
    claw_close_axis = joystick.get_axis(5)  # Right trigger
    elbow_up = joystick.get_hat(0)[1] == 1   # D-Pad up
    elbow_down = joystick.get_hat(0)[1] == -1 # D-Pad down
    gantry_up = joystick.get_hat(0)[0] == 1   # D-Pad right
    gantry_down = joystick.get_hat(0)[0] == -1 # D-Pad left

    # Initialize PWMs at neutral position
    wrist_left_pwm = 128
    wrist_right_pwm = 128
    claw_pwm = 128

    # Claw control
    if claw_open_axis > 0:  # Left trigger partially/fully pressed
        claw_pwm = int((claw_open_axis + 1) * 127.5)
    elif claw_close_axis > 0:  # Right trigger partially/fully pressed
        claw_pwm = int(255 - ((claw_close_axis + 1) * 127.5))

    # Wrist control
    if wrist_up:
        wrist_left_pwm = 255
        wrist_right_pwm = 0
    elif wrist_down:
        wrist_left_pwm = 0
        wrist_right_pwm = 255
    elif wrist_max:
        wrist_left_pwm = 255
        wrist_right_pwm = 255
    elif wrist_min:
        wrist_left_pwm = 0
        wrist_right_pwm = 0

    # Shoulder, elbow, and gantry control
    shoulder_pwm = 255 if rotate_right else 0 if rotate_left else 128
    elbow_pwm = 255 if elbow_up else 0 if elbow_down else 128
    gantry_pwm = 255 if gantry_up else 0 if gantry_down else 128

    return [
        elbow_pwm,
        wrist_right_pwm,
        wrist_left_pwm,
        claw_pwm,
        gantry_pwm,
        shoulder_pwm
    ]

def construct_drive_packet(wheel_pwms):
    """Construct the drive command packet."""
    return f"D_{'_'.join(map(str, wheel_pwms))}"

def construct_arm_packet(arm_pwms):
    """Construct the arm command packet."""
    return f"A_{'_'.join(map(str, arm_pwms))}"
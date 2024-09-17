import pygame

def map_axis_to_pwm(axis_value):
    """Map joystick axis value to PWM range."""
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
    """Get PWM values for rover wheels based on joystick input."""
    left_wheel_axis = joystick.get_axis(1)
    right_wheel_axis = joystick.get_axis(3)
    right_wheel_pwms = [map_axis_to_pwm(right_wheel_axis)] * 3
    left_wheel_pwms = [map_axis_to_pwm(left_wheel_axis)] * 3
    return right_wheel_pwms + left_wheel_pwms

def get_arm_pwm_values(joystick):
    """Get PWM values for arm components based on joystick input."""
    wrist_up = joystick.get_button(3)    # Y button
    wrist_down = joystick.get_button(0)  # A button
    wrist_left = joystick.get_button(2)  # X button
    wrist_right = joystick.get_button(1) # B button
    rotate_left = joystick.get_button(4)  # Left shoulder button
    rotate_right = joystick.get_button(5) # Right shoulder button
    claw_open = joystick.get_button(6)   # Left trigger
    claw_close = joystick.get_button(7)  # Right trigger
    elbow_up = joystick.get_hat(0)[1] == 1   # D-Pad up
    elbow_down = joystick.get_hat(0)[1] == -1 # D-Pad down
    gantry_up = joystick.get_hat(0)[0] == 1   # D-Pad right
    gantry_down = joystick.get_hat(0)[0] == -1 # D-Pad left

    wrist_left_pwm = map_axis_to_pwm(joystick.get_axis(2))  # Assuming axis 2 for wrist left
    wrist_right_pwm = map_axis_to_pwm(joystick.get_axis(5)) # Assuming axis 5 for wrist right

    if claw_open:
        claw_pwm = 255  # Open claw
    elif claw_close:
        claw_pwm = 0    # Close claw
    else:
        claw_pwm = 128  # Neutral position

    if wrist_left and wrist_right:
        # Spin wrist left and right
        wrist_left_pwm = 255
        wrist_right_pwm = 0
    elif wrist_left:
        # Spin wrist left
        wrist_left_pwm = 255
        wrist_right_pwm = 128
    elif wrist_right:
        # Spin wrist right
        wrist_left_pwm = 128
        wrist_right_pwm = 255
    else:
        wrist_left_pwm = 128
        wrist_right_pwm = 128

    shoulder_pwm = 255 if rotate_right else 0 if rotate_left else 128
    elbow_pwm = 255 if elbow_up else 0 if elbow_down else 128
    gantry_pwm = 255 if gantry_up else 0 if gantry_down else 128

    return [
        max(0, min(255, elbow_pwm)),
        max(0, min(255, wrist_right_pwm)),
        max(0, min(255, wrist_left_pwm)),
        max(0, min(255, claw_pwm)),
        max(0, min(255, gantry_pwm)),
        max(0, min(255, shoulder_pwm))
    ]

def construct_drive_packet(wheel_pwms):
    """Construct drive command packet."""
    packet = f"D_{'_'.join(map(str, wheel_pwms))}"
    return packet

def construct_arm_packet(arm_pwms):
    """Construct arm command packet."""
    packet = f"A_{'_'.join(map(str, arm_pwms))}"
    return packet
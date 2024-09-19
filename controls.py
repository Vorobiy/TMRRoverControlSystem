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

    wrist_left_pwm = 128 
    wrist_right_pwm = 128
    claw_pwm = 128

    if claw_open_axis > 0:  # Left trigger partially/fully pressed
        claw_pwm = int((claw_open_axis + 1) * 127.5)
    elif claw_close_axis > 0:  # Right trigger partially/fully pressed
        claw_pwm = int(255 - ((claw_close_axis + 1) * 127.5))
    else:
        claw_pwm = 128

    if wrist_up:  # X button pressed for wrist up
        wrist_left_pwm = 255
        wrist_right_pwm = 0
    elif wrist_down:  # B button pressed for wrist down
        wrist_left_pwm = 0
        wrist_right_pwm = 255
    elif wrist_max:  # A button pressed for max PWM (128-255)
        wrist_left_pwm = 255
        wrist_right_pwm = 255
    elif wrist_min:  # Y button pressed for min PWM (0-128)
        wrist_left_pwm = 0
        wrist_right_pwm = 0

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
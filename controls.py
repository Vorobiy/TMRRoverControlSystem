import pygame

# Initialize pygame for joystick handling
pygame.init()

# Function to map joystick axis values (-1 to 1) to PWM values (0 to 255)
def map_axis_to_pwm(axis_value):
    # Mapping axis (-1 to 1) to PWM (0 to 255), with 128 being neutral
    return int((axis_value + 1) * 127.5)

# Function to initialize the joystick
def init_joystick():
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        raise RuntimeError("No joysticks detected.")
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

# Function to get joystick values and convert to PWM for the wheels
def get_wheel_pwm_values(joystick):
    # Example: replace axis indices with actual mapping for your setup
    right_wheel_axis = joystick.get_axis(0)  # Right wheel axis
    left_wheel_axis = joystick.get_axis(1)   # Left wheel axis

    # Map axis to PWM values
    rightWheel1 = map_axis_to_pwm(right_wheel_axis)
    rightWheel2 = map_axis_to_pwm(right_wheel_axis)
    rightWheel3 = map_axis_to_pwm(right_wheel_axis)

    leftWheel1 = map_axis_to_pwm(left_wheel_axis)
    leftWheel2 = map_axis_to_pwm(left_wheel_axis)
    leftWheel3 = map_axis_to_pwm(left_wheel_axis)

    return rightWheel1, rightWheel2, rightWheel3, leftWheel1, leftWheel2, leftWheel3
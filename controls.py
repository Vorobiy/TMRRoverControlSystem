import pygame

# Function to map joystick axis values (-1 to 1) to PWM values (0 to 255)
def map_axis_to_pwm(axis_value):
    # Mapping axis (-1 to 1) to PWM (0 to 255), with 128 being neutral
    return int((axis_value + 1) * 127.5)

# Function to initialize the joystick
def init_joystick():
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    return joystick

# Function to get joystick values and convert to PWM for the wheels
def get_wheel_pwm_values(joystick):
    # Left joystick vertical axis (axis 1) controls the left wheels
    left_wheel_axis = joystick.get_axis(1)

    # Right joystick vertical axis (axis 4) controls the right wheels
    right_wheel_axis = joystick.get_axis(3)

    # Map axis to PWM values
    rightWheel1 = map_axis_to_pwm(right_wheel_axis)
    rightWheel2 = map_axis_to_pwm(right_wheel_axis)
    rightWheel3 = map_axis_to_pwm(right_wheel_axis)

    leftWheel1 = map_axis_to_pwm(left_wheel_axis)
    leftWheel2 = map_axis_to_pwm(left_wheel_axis)
    leftWheel3 = map_axis_to_pwm(left_wheel_axis)

    return rightWheel1, rightWheel2, rightWheel3, leftWheel1, leftWheel2, leftWheel3
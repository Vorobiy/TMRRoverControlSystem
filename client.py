import pygame
import socket
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

def setup_client_connection():
    """Setup socket connection to the server."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))
        print("Connected to server.")
        return client_socket
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return None

def has_input_changed(prev_state, current_state):
    """Check if the input state has changed."""
    return prev_state != current_state

def send_commands(client_socket):
    """Send commands to the server based on joystick input."""
    pygame.init()
    pygame.joystick.init()

    joystick = init_joystick()

    clock = pygame.time.Clock()
    running = True

    # Store previous states for comparison
    prev_wheel_pwms = None
    prev_arm_pwms = None

    while running:
        pygame.event.pump()  # Process internal pygame events

        # Get PWM values for wheels and arms from joystick
        wheel_pwms = get_wheel_pwm_values(joystick)
        arm_pwms = get_arm_pwm_values(joystick)

        # Only send data if there has been a change in input
        if has_input_changed(prev_wheel_pwms, wheel_pwms):
            # Construct drive command
            drive_command = construct_drive_packet(wheel_pwms)

            # Send the drive command
            try:
                client_socket.sendall(drive_command.encode())
                print(f"Sent drive command: {drive_command}")
            except Exception as e:
                print(f"Failed to send drive command: {e}")
                break  # Stop if we can't send data

            # Update the previous state for wheels
            prev_wheel_pwms = wheel_pwms

        if has_input_changed(prev_arm_pwms, arm_pwms):
            # Construct arm command
            arm_command = construct_arm_packet(arm_pwms)

            # Send the arm command
            try:
                client_socket.sendall(arm_command.encode())
                print(f"Sent arm command: {arm_command}")
            except Exception as e:
                print(f"Failed to send arm command: {e}")
                break  # Stop if we can't send data

            # Update the previous state for arms
            prev_arm_pwms = arm_pwms

        # Event handling for quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control the rate of sending commands (10 times per second)
        clock.tick(10)

    pygame.quit()
    client_socket.close()

if __name__ == "__main__":
    client_socket = setup_client_connection()
    if client_socket:
        send_commands(client_socket)
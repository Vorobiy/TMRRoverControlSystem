import socket
import pygame
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

def send_commands():
    """Send commands to the server based on joystick input."""
    pygame.init()
    pygame.joystick.init()
    joystick = init_joystick()

    current_drive_command = None
    current_arm_command = None

    # Connect to the TCP server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 8000))

    try:
        while True:
            pygame.event.pump()  # Event handler for pygame

            # Get PWM values for wheels and arms from joystick
            wheel_pwms = get_wheel_pwm_values(joystick)
            arm_pwms = get_arm_pwm_values(joystick)

            # Construct commands
            new_drive_command = construct_drive_packet(wheel_pwms)
            new_arm_command = construct_arm_packet(arm_pwms)

            # Update commands only if there's a change
            if new_drive_command != current_drive_command:
                current_drive_command = new_drive_command
                # Add newline to mark the end of the packet
                server_socket.send((current_drive_command + "\n").encode())

            if new_arm_command != current_arm_command:
                current_arm_command = new_arm_command
                # Add newline to mark the end of the packet
                server_socket.send((current_arm_command + "\n").encode())

            pygame.time.wait(100)  # Wait for 100ms before sending again

    except KeyboardInterrupt:
        print("Client disconnected")
    finally:
        server_socket.close()

if __name__ == "__main__":
    send_commands()
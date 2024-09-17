import pygame
import socket
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

def setup_client_connection():
    """Setup socket connection to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  # Replace with actual host and port
    return client_socket

def send_commands(client_socket):
    """Send commands to the server based on joystick input."""
    pygame.init()
    pygame.joystick.init()

    joystick = init_joystick()

    running = True
    while running:
        pygame.event.pump()

        wheel_pwms = get_wheel_pwm_values(joystick)
        arm_pwms = get_arm_pwm_values(joystick)

        drive_command = construct_drive_packet(wheel_pwms)
        arm_command = construct_arm_packet(arm_pwms)

        # Send both commands on the same line, separated by a delimiter
        combined_command = f"{drive_command}|{arm_command}\n"
        client_socket.sendall(combined_command.encode())
        print(f"Sent Combined Command: {combined_command.strip()}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.Clock().tick(10)  # Adjust the rate of sending commands

    pygame.quit()

if __name__ == "__main__":
    client_socket = setup_client_connection()
    send_commands(client_socket)
import pygame
import socket
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

def setup_client_connection():
    """Setup socket connection to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))
    return client_socket

def send_commands(client_socket):
    """Send commands to the server based on joystick input."""
    pygame.init()
    pygame.joystick.init()

    joystick = init_joystick()

    running = True
    while running:
        pygame.event.pump()

        # Get PWM values for wheels and arms from joystick
        wheel_pwms = get_wheel_pwm_values(joystick)
        arm_pwms = get_arm_pwm_values(joystick)

        # Construct drive and arm commands separately
        drive_command = construct_drive_packet(wheel_pwms)  
        arm_command = construct_arm_packet(arm_pwms)   

        # Send the drive command first
        client_socket.sendall(drive_command.encode())
        print(f"Sent Drive Command: {drive_command.strip()}")

        # Send the arm command separately
        client_socket.sendall(arm_command.encode())
        print(f"Sent Arm Command: {arm_command.strip()}")

        # Check for quitting the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Control the rate of sending commands (10 times per second)
        pygame.time.Clock().tick(10)

    pygame.quit()

if __name__ == "__main__":
    client_socket = setup_client_connection()
    send_commands(client_socket)
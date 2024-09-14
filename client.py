import socket
import pygame
from controls import init_joystick, get_wheel_pwm_values

# Function to create the drive command string
def create_drive_command(rightWheel1, rightWheel2, rightWheel3, leftWheel1, leftWheel2, leftWheel3):
    return f"D_{rightWheel1}_{rightWheel2}_{rightWheel3}_{leftWheel1}_{leftWheel2}_{leftWheel3}"

# Setup the socket connection
def setup_client_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  # Replace with actual host and port
    return client_socket

# Function to send drive commands to the server
def send_drive_commands(client_socket):
    joystick = init_joystick()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get PWM values for the wheels
        rightWheel1, rightWheel2, rightWheel3, leftWheel1, leftWheel2, leftWheel3 = get_wheel_pwm_values(joystick)

        # Create drive command packet
        drive_command = create_drive_command(rightWheel1, rightWheel2, rightWheel3, leftWheel1, leftWheel2, leftWheel3)
        print(f"Sending: {drive_command}")  # Debugging output

        # Send the command to the server
        client_socket.sendall(drive_command.encode())

        # Limit the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    client_socket = setup_client_connection()
    send_drive_commands(client_socket)
    client_socket.close()
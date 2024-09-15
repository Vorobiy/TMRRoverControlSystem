import socket
import pygame
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

# Function to create the drive command string
def create_drive_command(wheels):
    return f"D_{wheels[0]}_{wheels[1]}_{wheels[2]}_{wheels[3]}_{wheels[4]}_{wheels[5]}"

# Function to create the arm command string
def create_arm_command(arm):
    return f"A_{arm[0]}_{arm[1]}_{arm[2]}_{arm[3]}_{arm[4]}_{arm[5]}"

# Setup the socket connection
def setup_client_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))  # Replace with actual host and port
    return client_socket

# Function to send combined commands (drive + arm) to the server
def send_commands(client_socket):
    pygame.init()
    pygame.joystick.init()  # Initialize the joystick module

    joystick = init_joystick()  # Initialize joystick

    running = True
    while running:
        pygame.event.pump()  # Process event queue

        # Get PWM values for the wheels and arm
        wheel_pwms = get_wheel_pwm_values(joystick)
        arm_pwms = get_arm_pwm_values(joystick)

        # Create combined command packet
        drive_command = create_drive_command(wheel_pwms)
        arm_command = create_arm_command(arm_pwms)
        combined_command = f"{drive_command} {arm_command}"  # Combine drive and arm commands side by side
        print(f"Sending: {combined_command}")

        # Send the combined command to the server
        client_socket.sendall(combined_command.encode())

        # Control exit with a quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limit the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()

if __name__ == "__main__":
    client_socket = setup_client_connection()
    send_commands(client_socket)
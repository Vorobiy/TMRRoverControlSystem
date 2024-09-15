import socket

# Setup server connection
def setup_server_connection():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))  # Replace with actual host and port
    server_socket.listen(1)  # Listen for one connection
    print("Server listening for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    return conn

# Function to handle received commands (both drive and arm in one packet)
def handle_commands(conn):
    running = True
    while running:
        # Receive combined data from client
        data = conn.recv(1024)
        if not data:
            break

        # Decode the combined command
        combined_command = data.decode()

        # Split the drive and arm commands by checking the starting character
        drive_command = combined_command.split('A_')[0].strip()
        arm_command = 'A_' + combined_command.split('A_')[1].strip() if 'A_' in combined_command else ''

        # Process drive and arm commands
        if drive_command.startswith("D_"):
            print(f"Drive Command Received: {drive_command}")
        if arm_command.startswith("A_"):
            print(f"Arm Command Received: {arm_command}")

if __name__ == "__main__":
    conn = setup_server_connection()
    handle_commands(conn)
    conn.close()
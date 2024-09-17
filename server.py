import socket

def setup_server_connection():
    """Setup socket connection for the server."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))  # Replace with actual host and port
    server_socket.listen(1)  # Listen for one connection
    print("Server listening for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    return conn

def handle_commands(conn):
    """Handle incoming commands from the client."""
    running = True
    while running:
        data = conn.recv(1024)
        if not data:
            break

        # Decode the received data and split it using the delimiter
        combined_command = data.decode().strip()
        if '|' in combined_command:
            drive_command, arm_command = combined_command.split('|', 1)
            print(f"Drive Command Received: {drive_command}")
            print(f"Arm Command Received: {arm_command}")

if __name__ == "__main__":
    conn = setup_server_connection()
    handle_commands(conn)
    conn.close()
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

# Function to handle received commands
def handle_drive_commands(conn):
    running = True
    while running:
        # Receive data from client
        data = conn.recv(1024)
        if not data:
            break

        # Decode and print the command (this is where you'd process the command)
        drive_command = data.decode()
        print(f"Received: {drive_command}")

if __name__ == "__main__":
    conn = setup_server_connection()
    handle_drive_commands(conn)
    conn.close()
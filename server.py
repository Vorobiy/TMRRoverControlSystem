import socket

def handle_commands(conn):
    """Handle incoming commands from the client."""
    try:
        running = True
        while running:
            data = conn.recv(1024)
            if not data:
                break

            # Decode the received data
            command = data.decode().strip()

            # Handle the command based on its prefix (A_ for Arm, D_ for Drive)
            if command.startswith('A_'):
                print(f"{command}")
            elif command.startswith('D_'):
                print(f"{command}")
            else:
                print(f"Unknown Command Received: {command}")
    except Exception as e:
        print(f"Error handling command: {e}")
    finally:
        conn.close()

def start_server():
    """Start the server to listen for incoming connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("Server listening on port 9999...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        handle_commands(conn)

if __name__ == "__main__":
    start_server()
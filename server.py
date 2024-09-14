import socket

# Function to handle incoming client connections and receive data
def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Client disconnected
            print(f"Received: {data}")  # Output the received drive command
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

    client_socket.close()

# Setup the server
def setup_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))  # Bind to localhost and port 9999
    server_socket.listen(1)
    print("Server listening on port 9999...")
    return server_socket

if __name__ == "__main__":
    server_socket = setup_server()
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        handle_client(client_socket)
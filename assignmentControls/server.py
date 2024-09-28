import socket
import select

clients = set()

def handle_commands():
    """Start the TCP server to handle incoming commands from clients."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 8000))
    server_socket.listen(5)

    print("TCP Server listening on port 8000...")

    while True:
        # Use select to handle multiple clients
        readable, _, _ = select.select([server_socket] + list(clients), [], [])

        for s in readable:
            if s is server_socket:
                client_socket, _ = server_socket.accept()
                clients.add(client_socket)
                print(f"Client {client_socket} connected")
            else:
                try:
                    data = s.recv(1024).decode()

                    if not data:
                        raise ConnectionResetError

                    # Split the incoming data by newline characters (packet delimiter)
                    packets = data.split("\n")

                    # Process each packet
                    for packet in packets:
                        if packet.strip():  # Ignore empty packets
                            print(f"Received command: {packet}")

                            # Broadcast to all clients except the sender
                            for client in clients:
                                if client != s:
                                    client.send((packet + "\n").encode())
                except (ConnectionResetError, ConnectionAbortedError):
                    print(f"Client {s} disconnected")
                    clients.remove(s)
                    s.close()

if __name__ == "__main__":
    handle_commands()
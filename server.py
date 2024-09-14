import socket

# Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind(('localhost', 8080))

# Start listening for connections (max 5 clients can wait)
server_socket.listen(5)
print('Waiting for a connection...')

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

# Receive data
data = client_socket.recv(1024)  # Buffer size is 1024 bytes
print(f"Received: {data.decode()}")

# Send a response
client_socket.send(b"Hello, Client!")

# Close the connection
client_socket.close()
server_socket.close()
import socket

# Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8080))

# Send data
client_socket.send(b"Hello, Server!")

# Receive a response
response = client_socket.recv(1024)
print(f"Server response: {response.decode()}")

# Close the connection
client_socket.close()

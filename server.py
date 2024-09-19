def handle_commands(conn):
    """Handle incoming commands from the client."""
    running = True
    while running:
        data = conn.recv(1024)
        if not data:
            break

        # Decode the received data
        command = data.decode().strip()

        # Handle the command based on its prefix (A_ for Arm, D_ for Drive)
        if command.startswith('A_'):
            print(f"Arm Command Received: {command}")
        elif command.startswith('D_'):
            print(f"Drive Command Received: {command}")
        else:
            print(f"Unknown Command Received: {command}")
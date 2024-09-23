import asyncio
import websockets

clients = set()

async def handle_commands(websocket, path):
    """Handle incoming commands from the client."""
    clients.add(websocket)
    try:
        while True:
            data = await websocket.recv()
            # Broadcast to all clients
            for client in clients:
                if client != websocket:
                    await client.send(data)
            print(f"Received command: {data}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        clients.remove(websocket)

async def start_server():
    """Start the WebSocket server."""
    print("WebSocket Server listening on port 8000...")
    async with websockets.serve(handle_commands, "localhost", 8000):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(start_server())
import asyncio
import websockets
import pygame
from controls import init_joystick, get_wheel_pwm_values, get_arm_pwm_values, construct_drive_packet, construct_arm_packet

async def send_commands(websocket):
    """Send commands to the server based on joystick input."""
    pygame.init()
    pygame.joystick.init()
    joystick = init_joystick()

    current_drive_command = None
    current_arm_command = None

    while True:
        pygame.event.pump()  # event handler for pygame

        # Get PWM values for wheels and arms from joystick
        wheel_pwms = get_wheel_pwm_values(joystick)
        arm_pwms = get_arm_pwm_values(joystick)

        # Construct commands
        new_drive_command = construct_drive_packet(wheel_pwms)
        new_arm_command = construct_arm_packet(arm_pwms)

        # Update commands only if there's a change
        if new_drive_command != current_drive_command:
            current_drive_command = new_drive_command
            await websocket.send(current_drive_command)

        if new_arm_command != current_arm_command:
            current_arm_command = new_arm_command
            await websocket.send(current_arm_command)

        await asyncio.sleep(0.1)  # Throttle to reduce spam

async def main():
    async with websockets.connect('ws://localhost:8000') as websocket:
        await send_commands(websocket)

if __name__ == "__main__":
    asyncio.run(main())
# Rover Control System

This project is a control system for the 2023 rover, which uses a video game controller to control the rover's 12 motors (6 for driving and 6 for arm control). The system sends drive and arm command packets from the client to the server using Python's socket library.

## Features
- **Joystick Input**: Control the rover using a game controller (Xbox/PlayStation).
- **Motor Commands**: Send real-time commands to drive wheels and control the rover's arm.
- **Socket Communication**: Uses Python's socket library for client-server communication.
- **PWM Control**: Map joystick and button inputs to PWM values for controlling motors.

## Dependencies
To run this project, you will need the following Python libraries:

- `pygame`: For joystick input
- `socket`: For client-server communication

You can install the required dependencies using the following command:

```bash
pip install pygame
```

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
- `websockets`: For client-server communication
- `npm`: For package manager
- `Node.js`: For package Managing

You can install the required dependencies using the following command:

```bash
pip install pygame
```
## Steps to Launch controls only:
**Step 1**: Clone Git Repo:
```bash
git clone https://github.com/vorobiy/TMRRoverControlSystem.git
```
**Step 2**: Run server:
```bash
cd assignmentControls
py server.py
```
**Step 3**: Run client in new terminal:
```bash
cd assignmentControls
py client.py
```
If you now go back to the server.py folder, you'll see the packet output and if you stay at client.py you'll see the increase and decrease in speed if you press the two small buttons underneath the xbox controller.

## Steps to Launch part A:
**Step 1**: Launch server:
```bash
cd part_A
py server.py
```
**Step 2**: Run client in new terminal:
```bash
cd part_A/rover_ui
py client.py
```

**Step 3**: Run React + Vite in new terminal:
```bash
cd part_A/rover_ui
npm run dev
```





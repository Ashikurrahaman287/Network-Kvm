# Simple KVM in Python

## Overview
This project implements a simple Keyboard-Video-Mouse (KVM) control system in Python. It allows you to control the mouse movement, left-click, and keyboard input on a remote machine using a client script.

## Features
- Control mouse movement by specifying coordinates (x,y).
- Perform a left-click remotely.
- Send keyboard input to the remote machine.

## Prerequisites
- Python 3.x installed on both the server and client machines.
- `pyautogui` and `keyboard` Python libraries installed. You can install them using pip:
  ```
  pip install pyautogui keyboard
  ```

## Usage
1. **Server Setup**:
   - Run the `server.py` script on the machine you want to control remotely.
   - Specify the IP address and port to listen on in the script.

2. **Client Setup**:
   - Run the `client.py` script on the machine from which you want to control the server.
   - Enter commands when prompted:
     - `x,y` for mouse movement.
     - `L` for a left-click.
     - Any text for keyboard input.

3. **Control**:
   - Use the client script to send commands to the server and control the mouse and keyboard remotely.

## Troubleshooting
- If you encounter any connection issues, ensure that the server script is running and listening on the correct IP address and port.
- Check for firewall or antivirus software blocking the connection.
- Verify network connectivity between the client and server machines.

## Disclaimer
This project is intended for educational purposes and may not be suitable for production environments. Use it responsibly and ensure proper security measures are in place.
For any Help - Ashik@spudblocks.com

---

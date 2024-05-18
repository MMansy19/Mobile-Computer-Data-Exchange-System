# Mobile-Computer Data Exchange System

## Overview

This project aims to facilitate data exchange between a mobile device (Android) and a computer using a Python-based server-client architecture. The system utilizes Kivy for building the Android application and Python's socket module for communication between the mobile device and the computer.

## Skills & Technologies

- **Python:** Used for developing both the server-side and GUI application.
- **Kivy:** Framework for building the mobile application with Python.
- **Socket Programming:** Implemented for communication between the mobile application and the server.
- **Android Development:** Utilized for creating the mobile application.
- **GUI Development:** Created a graphical user interface application for the computer using Kivy.
- **Networking:** Established connections over the local network for data exchange.
- **Version Control (Git):** Managed project versions and collaboration using Git.

## How It Works

The system comprises two main components: the mobile application running on Android and the server running on the computer.

### Mobile Application (Kivy)

The mobile application is built using Kivy, a Python framework for developing multi-touch applications. It allows users to input data on the mobile device, which is then sent to the computer over the local network.

### Server (server.py)

The server is a Python script (`server.py`) running on the computer. It listens for incoming connections from the mobile application and processes the data received.

### Data Exchange Protocol

The mobile application sends data to the server using a socket connection established over the local network. The server listens for incoming connections and receives the data sent by the mobile application. Once data is received, the server processes it as required.

### GUI Application (main.py)

The GUI application (`main.py`) running on the computer is responsible for displaying the received data in a graphical user interface (GUI). It communicates with the server to fetch the data and update the GUI accordingly.

## Connecting to the Server

To connect the mobile application to the server, follow these steps:

1. Ensure both the mobile device and the computer are connected to the same local network.
2. Launch the mobile application and input the IP address of the computer running the server.
3. The mobile application will establish a socket connection with the server using the specified IP address and port.

<!-- ## Contributors
- John Doe (@johndoe)
- Jane Smith (@janesmith) -->

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

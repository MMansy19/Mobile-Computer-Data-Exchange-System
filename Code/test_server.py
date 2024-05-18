import socket
import threading
import random
import time

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    while True:
        # Receive data from the client
        request = client_socket.recv(1024).decode()
        if request == 'get_heart_rate':
            # Simulate heart rate data
            heart_rate_data = ';'.join([str(random.randint(60, 120)) for _ in range(3)])
            # Send heart rate data to the client
            client_socket.send(heart_rate_data.encode())
            time.sleep(1)  # Simulate delay
        else:
            break
    print(f"Connection with {client_address} closed.")
    client_socket.close()

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5555))
server_socket.listen(5)

print("Server listening on port 5555...")

# Accept incoming connections and handle them in separate threads
while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

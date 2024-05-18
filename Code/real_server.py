import socket
import threading

# Store heart rate data for three patients
heart_rate_data = ["0", "0", "0"]

def handle_client(client_socket):
    global heart_rate_data
    try:
        while True:
            request = client_socket.recv(1024).decode()
            if not request:
                break
            if request == 'get_heart_rate':
                client_socket.send(';'.join(heart_rate_data).encode())
            else:
                heart_rate_data[:] = request.split(';')
                print(f"Updated heart rates: {heart_rate_data}")
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Server listening on port 5555")
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == '__main__':
    main()

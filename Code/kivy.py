
# You Run this code on your Android device Not on your computer


# Import necessary modules
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import socket
import random
import time
import threading

# Define the main layout
class HeartRateMonitorApp(App):

    # Function to generate random heart rate data
    def generate_heart_rate_data(self):
        return ';'.join(str(random.randint(60, 120)) for _ in range(3))

    # Function to send heart rate data to the server
    def send_heart_rate_data(self):
        try:
            server_address = ('192.168.1.18', 5555)  # Use your computer's IP address
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)
            print("Connected to server")
            while True:
                heart_rate_data = self.generate_heart_rate_data()
                print(f"Sending heart rate data: {heart_rate_data}")
                client_socket.send(heart_rate_data.encode())
                time.sleep(1)  # Send data every second
        except Exception as e:
            print(f"Error sending heart rate data: {e}")
        finally:
            client_socket.close()
            print("Closed connection to server")

    # Function to start sending heart rate data in a separate thread
    def start_sending_data(self):
        threading.Thread(target=self.send_heart_rate_data).start()

    # Build the app interface
    def build(self):
        # Start sending heart rate data
        self.start_sending_data()
        # Create a label to display status
        status_label = Label(text=f"Sending heart rate data to server... \n {self.generate_heart_rate_data()}", font_size='20sp')
        # Create a layout and add the label to it
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(status_label)
        return layout

# Run the app
if __name__ == '__main__':
    HeartRateMonitorApp().run()

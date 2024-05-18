import tkinter as tk
from tkinter import messagebox
import socket

# Function to fetch heart rate data from server
def fetch_heart_rate():
    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.1.18', 5555))  # Use your computer's IP address
        # Send a request for heart rate data
        client_socket.send(b'get_heart_rate')
        # Receive heart rate data from the server
        data = client_socket.recv(1024).decode()
        client_socket.close()
        return data
    except Exception as e:
        print(f"Error fetching heart rate data: {e}")
        return ""

# Function to update the GUI with new heart rate data
# Function to update the GUI with new heart rate data
def update_gui():
    data = fetch_heart_rate()
    if data:
        data = data.split(';')
        if len(data) != len(patient_hr_labels):
            print(f"Warning: Received {len(data)} heart rate values, but expected {len(patient_hr_labels)}")
        for i, heart_rate in enumerate(data):
            if i < len(patient_hr_labels):  # Ensure we don't go out of bounds
                if heart_rate:
                    patient_hr_labels[i].config(text=f"{heart_rate} bpm")
                    if int(heart_rate) > 115:  # Threshold for hypertension
                        alert_label.config(text=f"ALERT: Patient {i+1} is hypertensive! (Heart Rate: {heart_rate} bpm)", fg="#e74c3c")
                        root.bell()  # Play system alert sound
                        messagebox.showwarning("Hypertension Alert", f"Patient {i+1} is hypertensive! Heart Rate: {heart_rate} bpm")
                    else:
                        alert_label.config(text="")
    else:
        print("No data received")
    root.after(1000, update_gui)  # Update every second
# Set up the GUI
root = tk.Tk()
root.title("ICU Heart Rate Monitor")
root.geometry("400x250")
root.resizable(False, False)  # Disable window resizing

# Header
header_label = tk.Label(root, text="ICU Heart Rate Monitor", font=("Helvetica", 18, "bold"), pady=10)
header_label.pack()

# Patient Frame
patient_frame = tk.Frame(root)
patient_frame.pack()

patient_hr_labels = []
for i in range(3):
    patient_label = tk.Label(patient_frame, text=f"Patient {i+1}:", font=("Helvetica", 14, "bold"), pady=5)
    patient_label.grid(row=i, column=0, padx=(20, 5), pady=5, sticky="w")
    hr_label = tk.Label(patient_frame, text="-- bpm", font=("Helvetica", 12), padx=5)
    hr_label.grid(row=i, column=1, padx=5, pady=5)
    patient_hr_labels.append(hr_label)

# Alert Label
alert_label = tk.Label(root, text="", font=("Helvetica", 12), fg="#e74c3c")
alert_label.pack()

# Function to gracefully close the application
def close_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", close_app)  # Handle window close event

# Start updating GUI
root.after(2000, update_gui)
root.mainloop()

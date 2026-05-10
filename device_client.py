import socket
import json
import random
import time

HOST = '127.0.0.1'
PORT = 12000

DEVICE_ID = f"router_{random.randint(1,100)}"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"{DEVICE_ID} connected to server.")

while True:
    telemetry_data = {
        "device_id": DEVICE_ID,
        "status": "online",
        "temperature": random.randint(35, 60),
        "cpu_usage": random.randint(10, 90)
    }

    message = json.dumps(telemetry_data) # Convert into JSON

    client_socket.send(message.encode())

    print(f"Sent: {message}")

    time.sleep(3)
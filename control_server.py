import socket
import threading
import json

HOST = '127.0.0.1'
PORT = 12000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) 
server_socket.listen(5) # Allow up to 5 unaccepted connections before refusing.

print(f"Control server listening on {HOST}:{PORT}")

def handle_device(client_socket, address):
    print(f"New device connected: {address}")

    while True:
        try:
            data = client_socket.recv(1024) # 1024 is max data 
            
            if not data:
                break

            telemetry = json.loads(data.decode())

            print(
                f"Device: {telemetry['device_id']} | "
                f"Status: {telemetry['status']} | "
                f"Temperature: {telemetry['temperature']}C | "
                f"CPU Usage: {telemetry['cpu_usage']}%"
            )
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print(f"Connection closed: {address}")
    client_socket.close()

while True:
    client_socket, addr = server_socket.accept()
    
    device_thread = threading.Thread(
        target=handle_device,
        args=(client_socket, addr)
    )

    device_thread.start()
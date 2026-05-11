import socket
import threading
import json
from datetime import datetime, UTC

HOST = '127.0.0.1'
PORT = 12000
LOG_FILE = "device_logs.jsonl"

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

            log_event(
                event_type="TELEMETRY",
                device_id=telemetry['device_id'],
                addr=addr,
                data=telemetry
            )
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print(f"Connection closed: {address}")
    client_socket.close()


def log_event(event_type, device_id, addr, data=None):
    log_entry = {
        "timestamp": datetime.now(UTC).isoformat(),
        "event": event_type,
        "device_id": device_id,
        "address": str(addr),
        "data": data
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


while True:
    client_socket, addr = server_socket.accept()
    
    device_thread = threading.Thread(
        target=handle_device,
        args=(client_socket, addr)
    )

    device_thread.start()
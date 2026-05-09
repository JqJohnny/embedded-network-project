import socket
import json
import random
import time

HOST = '127.0.0.1'
PORT = 12000

DEVICE_ID = f"router_{random.randint(1,100)}"

print(f"{DEVICE_ID}")
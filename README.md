# Embedded Network Project

## Overview

This project is a Python-based socket programming application focused on networking and concurrent client-server communication concepts.

The project was originally developed as a school networking assignment focused on basic socket communication and is now being updated to better reflect real-world networking and embedded systems concepts. The updated version expands on the original project by adding multithreaded client handling, telemetry-style data using JSON, periodic device status updates, and simulated network-connected device communication. The original version of the project can be found [here](https://github.com/JqJohnny/sockets) for comparison of the new changes.


The application demonstrates:
- TCP socket communication
- multithreading
- client-server architecture
- concurrent device handling
- structured network communication

---

## Technologies Used

- Python
- TCP sockets
- threading
- JSON

---

## Files

### `control_server.py`
The central server responsible for:
- accepting incoming device connections
- handling multiple clients concurrently
- receiving and displaying telemetry-style data

---

### `device_client.py`
A simulated network-connected device that:
- connects to the control server
- periodically sends device status information
- simulates telemetry communication

---

## Concepts Demonstrated

- TCP/IP communication
- socket programming
- multithreaded server design
- client-server communication
- concurrent connection handling
- basic systems/network programming concepts

---

## Running the Project

### Start the Server

```bash
python control_server.py

# Basic Network Sniffer

## CodeAlpha Cyber Security Internship - Task 1

### Project Overview
The **Basic Network Sniffer** is a Python-based application that captures and analyzes network packets in real time. It helps users understand how data travels across a network by displaying important packet information such as source IP address, destination IP address, protocol type, and payload (when available).

This project is developed as part of the **CodeAlpha Cyber Security Internship**.

---

## Objectives

- Capture live network packets.
- Analyze packet structure and content.
- Understand network communication.
- Learn the basics of TCP/IP protocols.
- Display useful packet information in the terminal.

---

## Features

- Live packet capturing
- Displays Source IP Address
- Displays Destination IP Address
- Identifies Protocol (TCP, UDP, ICMP)
- Displays packet payload (if available)
- Real-time packet analysis
- Simple and beginner-friendly implementation

---

## Technologies Used

- Python 3.x
- Scapy Library
- Npcap (Windows)

---

## Project Structure

```
Basic_Network_Sniffer/
│
├── sniffer.py
├── requirements.txt
├── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Basic_Network_Sniffer.git
```

### 2. Navigate to the Project Folder

```bash
cd Basic_Network_Sniffer
```

### 3. Install Required Library

```bash
pip install scapy
```

### 4. Install Npcap (Windows)

Download and install **Npcap** from the official website.

During installation, enable:

- Install Npcap in WinPcap API-compatible Mode

---

## How to Run

Run the program with Administrator privileges.

```bash
python sniffer.py
```

Generate some network traffic by opening websites or using:

```bash
ping google.com
```

The program will capture and display packet information.

---

## Sample Output

```
==================================================
Source IP      : 192.168.1.5
Destination IP : 142.250.193.78
Protocol        : TCP

Payload:
b'GET / HTTP/1.1'
```

---

## Learning Outcomes

By completing this project, you will learn:

- Network Packet Sniffing
- Packet Structure Analysis
- IP Address Identification
- TCP/IP Protocol Basics
- Real-time Traffic Monitoring
- Python Networking with Scapy

---

## Future Enhancements

- Save captured packets to a PCAP file
- Filter packets by protocol
- Display MAC addresses
- Export packet details to CSV
- Create a graphical user interface (GUI)
- Real-time packet statistics dashboard

---

## Author

**NANDHITHA**

B.E. Cyber Security Student

CodeAlpha Cyber Security Intern

---

## Disclaimer

This project is developed for **educational purposes only**.

Use this tool only on networks that you own or have explicit permission to monitor. Unauthorized packet sniffing may violate privacy policies and applicable laws.

---

## License

This project is licensed under the MIT License.

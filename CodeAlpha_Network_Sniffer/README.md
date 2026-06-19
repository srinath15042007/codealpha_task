# Basic Network Sniffer using Python

## 📌 Project Description

This project is a simple Network Packet Sniffer developed using Python and Scapy.  
It captures live network packets and displays useful information such as:

- Source IP Address
- Destination IP Address
- Protocol Type (TCP/UDP/ICMP)
- Packet Length
- Timestamp

The project helps understand how network communication works and demonstrates basic packet analysis in cybersecurity.

---

## 🚀 Features

✅ Capture live network traffic  
✅ Detect TCP, UDP, and ICMP packets  
✅ Display source and destination IP addresses  
✅ Show packet size and timestamp  
✅ Real-time packet monitoring  

---

## 🛠 Technologies Used

- Python 3
- Scapy
- Linux / Ubuntu / Kali Linux
- VS Code

---


## ⚙ Installation

### Step 1: Install Python

Check Python version:

```bash
python3 --version
```

---

### Step 2: Install Scapy

```bash
pip3 install scapy
```

---

## ▶ Running the Program

Run the script with administrator privileges:

```bash
sudo python3 BNS.py
```

---

## 📜 Python Code

```python
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def process_packet(packet):

    if packet.haslayer(IP):

        print("=" * 60)

        print("Time:", datetime.now())

        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

        if packet.haslayer(TCP):
            protocol = "TCP"

        elif packet.haslayer(UDP):
            protocol = "UDP"

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        else:
            protocol = "Other"

        print("Protocol       :", protocol)
        print("Packet Length  :", len(packet), "bytes")

print("Starting Network Sniffer...")
print("Press CTRL+C to stop")

sniff(prn=process_packet, store=False)
```

---

## 📷 Sample Output

```text
============================================================
Time: 2026-06-19 10:30:20
Source IP      : 192.168.1.5
Destination IP : 142.250.183.46
Protocol       : TCP
Packet Length  : 74 bytes
```

---

## 🌐 Generate Traffic for Testing

Open another terminal and run:

```bash
ping google.com
```

or

```bash
curl https://google.com
```

---

## 🔒 Security Concepts Learned

- Packet Sniffing
- Network Monitoring
- Protocol Analysis
- Traffic Inspection
- Cybersecurity Basics

---

## 📌 Future Improvements

- Save packets to log files
- Add GUI using Tkinter
- Filter specific protocols
- Export captured data to CSV
- Detect suspicious packets

---

## 👨‍💻 Author

Your Name
SRINATH T G

CodeAlpha Cyber Security Internship

---

## 📄 License

This project is for educational purposes only.

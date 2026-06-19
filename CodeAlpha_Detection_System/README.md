# Network Intrusion Detection System (NIDS)

## 📌 Project Description

This project is a simple Network Intrusion Detection System (IDS) developed using Python and Scapy.  
It monitors network traffic in real time and detects suspicious activities such as:

- Port Scanning
- ICMP Flood Attacks
- Unusual Network Behavior

The system generates alerts whenever suspicious activity is detected.

---

## 🎯 Objectives

- Monitor network packets
- Detect intrusion attempts
- Identify suspicious traffic patterns
- Understand intrusion detection concepts
- Learn packet analysis and network security

---

## 🚀 Features

✅ Real-time packet monitoring  
✅ Detects port scanning attacks  
✅ Detects ICMP flood attacks  
✅ Generates security alerts  
✅ Lightweight and beginner-friendly IDS  

---

## 🛠 Technologies Used

- Python 3
- Scapy
- Linux / Ubuntu / Kali Linux
- VS Code

---

## ⚙ Installation

### Step 1: Check Python

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

Run the IDS with administrator privileges:

```bash
sudo python3 NIDS.py
```

---

## 📜 Python Code

```python
from scapy.all import sniff, IP, TCP, ICMP
from collections import defaultdict
from datetime import datetime

# Track scanned ports
scan_tracker = defaultdict(set)

# Track ICMP packets
icmp_counter = defaultdict(int)

PORT_SCAN_THRESHOLD = 10
ICMP_THRESHOLD = 20

def detect(packet):

    if not packet.haslayer(IP):
        return

    src_ip = packet[IP].src

    # Detect Port Scan
    if packet.haslayer(TCP):

        dst_port = packet[TCP].dport

        scan_tracker[src_ip].add(dst_port)

        if len(scan_tracker[src_ip]) > PORT_SCAN_THRESHOLD:

            print("\n[ALERT] Possible Port Scan Detected!")
            print(f"Source IP: {src_ip}")
            print(f"Time: {datetime.now()}")

            scan_tracker[src_ip].clear()

    # Detect ICMP Flood
    if packet.haslayer(ICMP):

        icmp_counter[src_ip] += 1

        if icmp_counter[src_ip] > ICMP_THRESHOLD:

            print("\n[ALERT] Possible ICMP Flood Detected!")
            print(f"Source IP: {src_ip}")
            print(f"Time: {datetime.now()}")

            icmp_counter[src_ip] = 0

print("Starting Intrusion Detection System...")
print("Monitoring Network Traffic...\n")

sniff(prn=detect, store=False)
```

---

## 📷 Sample Output

```text
Starting Intrusion Detection System...
Monitoring Network Traffic...

[ALERT] Possible Port Scan Detected!
Source IP: 127.0.0.1
Time: 2026-06-19 11:20:10

[ALERT] Possible ICMP Flood Detected!
Source IP: 127.0.0.1
Time: 2026-06-19 11:22:45
```

---

## 🌐 Testing the IDS

### Test Port Scan Detection

Install Nmap:

```bash
sudo apt install nmap
```

Run:

```bash
nmap -p 1-1000 localhost
```

---

### Test ICMP Flood Detection

```bash
ping -f 127.0.0.1
```

---

## 🔒 Security Concepts Learned

- Intrusion Detection
- Packet Inspection
- Port Scan Detection
- ICMP Flood Detection
- Network Monitoring
- Threat Analysis

---

## 📌 Future Improvements

- Email alerts
- GUI dashboard
- Log file generation
- Machine learning detection
- Real-time attack visualization
- Web-based monitoring panel

---

## 👨‍💻 Author

Your Name
SRINATH T G

CodeAlpha Cyber Security Internship

---

## 📄 Disclaimer

This project is created for educational purposes only.  
Do not use it for unauthorized network monitoring or malicious activities.

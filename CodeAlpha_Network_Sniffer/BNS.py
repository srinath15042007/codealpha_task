from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

LOG_FILE = "packets.log"

def process_packet(packet):

    if packet.haslayer(IP):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        src = packet[IP].src
        dst = packet[IP].dst

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "OTHER"

        length = len(packet)

        output = (
            f"[{timestamp}] "
            f"{protocol} | "
            f"Source: {src} -> Destination: {dst} "
            f"| Length: {length} bytes"
        )

        print(output)

        with open(LOG_FILE, "a") as file:
            file.write(output + "\n")

print("Starting Network Sniffer...")
print("Press CTRL+C to stop.\n")

sniff(prn=process_packet, store=False)

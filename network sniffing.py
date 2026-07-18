from scapy.all import sniff, IP
from datetime import datetime
def get_proto_name(proto):
    protocols = {
        1: "ICMP",
        6: "TCP",
        17: "UDP"
    }
    return protocols.get(proto, f"Other ({proto})")
def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("Packet Captured")
        print("=" * 50)
        print("Time           :", datetime.now().strftime("%H:%M:%S"))
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)
        print("Protocol Name  :", get_proto_name(packet[IP].proto))
        print("Packet Length  :", len(packet), "bytes")
        if packet.haslayer("Raw"):
            print("Payload        :", packet["Raw"].load)
        print()
try:
    print("Started Network Sniffing...")
    print("Capturing Packets...\n")
    sniff(prn=packet_callback, count=5)
    print("\nPacket Capture Completed Successfully!")
except PermissionError:
    print("Error: Run Command Prompt as Administrator.")
except Exception as e:
    print("Error:", e)

from scapy.all import sniff, hexdump

def packet_callback(packet):
    print(hexdump(packet))

sniff(prn=packet_callback, store=0)

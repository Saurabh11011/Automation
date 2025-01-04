import socket

def echo_server(host = "localhost",port = 9999):
    server_sok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # server_dsok = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server_sok.bind((host,port))
    server_sok.listen()
    print(f"serveris running on the particular port {host} and port = {port}")
    while True:
        client_sok, addr = server_sok.accept()
        print(f"connection from {addr}")
        while True:
            data = client_sok.recv(1024)
            if not data:
                break
            client_sok.sendall(data)
        client_sok.close()

echo_server()


# -------------------------------------------------------------------------

# to replay the packets
from scapy.all import rdpcap, send


def replay_packets(pcap_file='capture.pcap', destination_ip='localhost', destination_port=9999):
    packets = rdpcap(pcap_file)

    for packet in packets:
        # Send each packet to the echo server
        send(packet, iface="lo")  # Use the appropriate interface (e.g., "eth0", "lo" for localhost)

    print("Packets replayed successfully.")


if __name__ == "__main__":
    replay_packets()

# ---------------------------------------------------------------

# to replay the pcap on unix like system
# sudo tcpreplay --intf1=eth0 traffic.pcap

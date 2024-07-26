import socket
import threading
import sys

def scan_tcp_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"TCP Port {port}: Open")
        sock.close()
    except Exception as e:
        print(f"Error scanning TCP port {port}: {e}")

def scan_udp_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)
        result = sock.sendto(b"", (ip, port))
        try:
            data, addr = sock.recvfrom(1024)
            print(f"UDP Port {port}: Open")
        except socket.timeout:
            print(f"UDP Port {port}: Open or Filtered")
        sock.close()
    except Exception as e:
        print(f"Error scanning UDP port {port}: {e}")

def scan_ports(ip, start_port, end_port, protocol):
    threads = []
    for port in range(start_port, end_port + 1):
        if protocol == 'tcp':
            thread = threading.Thread(target=scan_tcp_port, args=(ip, port))
        elif protocol == 'udp':
            thread = threading.Thread(target=scan_udp_port, args=(ip, port))
        else:
            print("Unsupported protocol. Use 'tcp' or 'udp'.")
            return
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python port_scanner.py <IP> <start_port> <end_port> <protocol>")
        sys.exit(1)
    
    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    protocol = sys.argv[4].lower()

    scan_ports(ip, start_port, end_port, protocol)

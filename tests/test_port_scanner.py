import unittest
from src.port_scanner import scan_tcp_port, scan_udp_port

class TestPortScanner(unittest.TestCase):

    def test_scan_open_tcp_port(self):
        ip = "127.0.0.1"
        port = 80  # Commonly open port
        result = scan_tcp_port(ip, port)
        self.assertIsNone(result)  # Expecting no error for open port

    def test_scan_closed_tcp_port(self):
        ip = "127.0.0.1"
        port = 65535  # Commonly closed port
        result = scan_tcp_port(ip, port)
        self.assertIsNone(result)  # Expecting no error even if port is closed

    def test_scan_open_udp_port(self):
        ip = "127.0.0.1"
        port = 53  # Commonly open UDP port (DNS)
        result = scan_udp_port(ip, port)
        self.assertIsNone(result)  # Expecting no error for open port

    def test_scan_closed_udp_port(self):
        ip = "127.0.0.1"
        port = 65535  # Commonly closed port
        result = scan_udp_port(ip, port)
        self.assertIsNone(result)  # Expecting no error even if port is closed

if __name__ == '__main__':
    unittest.main()

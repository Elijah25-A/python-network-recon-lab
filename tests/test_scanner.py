import socket
import unittest
from src.scanner import scan

class ScannerTests(unittest.TestCase):
    def test_open_port(self):
        with socket.socket() as server:
            server.bind(("127.0.0.1", 0))
            server.listen()
            port = server.getsockname()[1]
            self.assertEqual(scan("127.0.0.1", [port]), [port])

    def test_nonlocal_rejected(self):
        with self.assertRaises(ValueError):
            scan("8.8.8.8", [80])

    def test_invalid_port_rejected(self):
        with self.assertRaises(ValueError):
            scan("127.0.0.1", [70000])

if __name__ == "__main__":
    unittest.main()

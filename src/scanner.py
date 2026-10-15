"""Localhost-only TCP connect scanner for a controlled security lab."""
import argparse
import ipaddress
import socket

def scan(host, ports, timeout=0.5):
    address = ipaddress.ip_address(socket.gethostbyname(host))
    if not address.is_loopback or address.version != 4:
        raise ValueError("Only IPv4 loopback targets are permitted")
    opened = []
    for port in ports:
        if not 1 <= port <= 65535:
            raise ValueError(f"Invalid port: {port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((str(address), port)) == 0:
                opened.append(port)
    return opened

def main():
    parser = argparse.ArgumentParser(description="Localhost TCP port assessment")
    parser.add_argument("--ports", default="8000,8080,22", help="Comma-separated ports")
    args = parser.parse_args()
    ports = [int(p.strip()) for p in args.ports.split(",")]
    print("Target: 127.0.0.1")
    for port in scan("127.0.0.1", ports):
        print(f"OPEN tcp/{port}")

if __name__ == "__main__":
    main()

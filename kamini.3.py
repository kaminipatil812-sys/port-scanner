import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        s.close()

    except Exception:
        pass


print(f"\nScanning {target}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))

print("\nScan complete")
print("Open ports:", open_ports)

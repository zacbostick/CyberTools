import socket
from concurrent.futures import ThreadPoolExecutor

target = '192.168.1.1'
port_range = (1, 65535)
max_threads = 100

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f'Port {port} is open')
    sock.close()

with ThreadPoolExecutor(max_workers=max_threads) as executor:
    for port in range(port_range[0], port_range[1] + 1):
        executor.submit(scan_port, port)

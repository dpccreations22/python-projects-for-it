import socket

host = "127.0.0.1"  # only scan machines you own or are allowed to test
ports = {22: "SSH", 80: "HTTP", 443: "HTTPS", 3389: "RDP", 5432: "Postgres"}

for port, name in ports.items():
    s = socket.socket()
    s.settimeout(0.5)
    is_open = s.connect_ex((host, port)) == 0
    s.close()
    print(f"{port:<6}{name:<10}{'OPEN' if is_open else 'closed'}")

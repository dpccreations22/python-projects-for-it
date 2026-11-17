import socket

servers = ["google.com", "github.com", "example.invalid"]

for host in servers:
    try:
        socket.create_connection((host, 443), timeout=3).close()
        print(f"UP    {host}")
    except OSError:
        print(f"DOWN  {host}")

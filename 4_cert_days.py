import socket
import ssl
import time

sites = ["google.com", "github.com", "wikipedia.org"]
context = ssl.create_default_context()

for site in sites:
    with socket.create_connection((site, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=site) as tls:
            expires = ssl.cert_time_to_seconds(tls.getpeercert()["notAfter"])
    days = int((expires - time.time()) // 86400)
    print(f"{site:<16}{days} days left" + ("  RENEW SOON!" if days < 30 else ""))

import ipaddress

ip = ipaddress.ip_address("192.168.122.1")

print(ip.version)
print(ip.is_loopback)
print(ip.is_private)
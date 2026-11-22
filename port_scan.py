import socket

services =  {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MYSQL"
}

def test_port(host, port, delay=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(delay)
        return s.connect_ex((host, port)) == 0

def scan(host, ports):
    opens = []
    for port in ports:
        if test_port(host, port):
            opens.append(port)
    return opens

host = "127.0.0.1"
opens = scan(host, range(1,1025))

print(f"Open ports on {host} :")
for p in opens:
    print(f" {p:5} {services.get(p, 'unknown service')}")
if not opens:
    print("no open port")
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(2)
    s.sendto("Coucou UDP".encode("utf-8",), ("127.0.0.1", 6000))
    try:
        reponse, adresse = s.recvfrom(1024)
        print(f"Réponse de {adresse}: {reponse.decode('utf-8')}")
    except socket.timeout:
        print("Pas de réponse du serveur. Le paquet s'est peut-être perdu.")

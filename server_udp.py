import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("127.0.0.1", 6000))
    print(f"Le serveur attend une connexion au port 6000")

    donnees, adresse = s.recvfrom(1024)
    print("Reçu de", adresse, ":", donnees.decode("utf-8"))
    s.sendto("Bien reçu".encode("utf-8"), adresse)
import socket

HOTE = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOTE, PORT))
    client.sendall("Bonjour serveur".encode("utf-8"))
    reponse = client.recv(1024)
    print("Réponse du serveur :", reponse.decode("utf-8"))
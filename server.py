import socket

HOTE = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serveur.bind((HOTE, PORT)) # on réserve l'adresse et le port
    serveur.listen() # on se met à l'écoute
    print("Serveur en attente sur le port", PORT)

    connexion, adresse = serveur.accept() # le programme attend ici
with connexion:
    print("Client connecté depuis", adresse)
    donnees = connexion.recv(1024)
    print("Message reçu :", donnees.decode("utf-8"))
    connexion.sendall("Bien reçu !".encode("utf-8"))
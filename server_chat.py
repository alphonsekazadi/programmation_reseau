import socket
import threading

HOTE = "127.0.0.1"
PORT = 5000
clients = []
verrou = threading.Lock()

def diffuser(message, expediteur):
    with verrou:
        for c in clients:
            if c is not expediteur: 
                try:
                    c.sendall(message)
                except OSError:
                    pass
def gerer_client(connexion, adresse):
    print("Nouveau client :", adresse)

    try:
        while True:
            donnees = connexion.recv(1024)
            if not donnees:
                break
            diffuser(donnees, connexion)
    except ConnectionResetError:
        pass
    finally:
        with verrou:
            clients.remove(connexion)
        connexion.close()
        print("Client parti :", adresse)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serveur.bind((HOTE, PORT))
    serveur.listen()
    print("Chat ouvert sur le port : ", PORT)

    while True:
        connexion, adresse = serveur.accept()
        with verrou:
            clients.append(connexion)
        threading.Thread(
            target=gerer_client,
            args=(connexion, adresse),
            daemon=True
        ).start()
import socket

HOTE = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.bind((HOTE, PORT))
    serveur.listen()
    print(f"Le serveur attend une connexion au port {PORT}")

    connexion, adresse = serveur.accept()

    with connexion:
        print("Le client est connecté depuis", adresse)
        donnees = connexion.recv(1024)
        print("Données reçues :", donnees.decode("utf-8"))
        connexion.sendall(input("Message à envoyer au client : ").encode("utf-8"))



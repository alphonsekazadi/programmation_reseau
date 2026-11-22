import socket
import threading

HOTE = "192.168.227.170"
PORT = 5000
pseudo = input("Ton pseudo ? : ")

def ecouter(s):
    while True:
        try:
            donnees = s.recv(1024)
        except OSError:
            break
        if not donnees:
            print("Le serveur a fermé la connexion.")
            break
        print(donnees.decode("utf-8"))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOTE, PORT))
    threading.Thread(target=ecouter, args=(s,),daemon=True).start()

    print("Tu es connecté. Ecris un message, ou tape /quitter pour partir.")
    while True:
        texte = input()
        if texte == "/quitter":
            break
        s.sendall(f"{pseudo} : {texte}".encode("utf-8"))
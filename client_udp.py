import socket

HOTE = "127.0.0.1"
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.settimeout(2)
    client.sendto(input("Message à envoyer au serveur : ").encode("utf-8"), (HOTE, PORT))

    try:
        reponse, adresse = client.recvfrom(1024)
        print(f"Réponse de {adresse}: {reponse.decode('utf-8')}")
    except socket.timeout:
        print("Pas de réponse du serveur. Le paquet s'est peut-être perdu.")
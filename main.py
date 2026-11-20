import socket

nomMachine = socket.gethostname()
print(f"Le nom de la machine : {nomMachine}")

ipMachine = socket.gethostbyname(nomMachine)
print(f"L'IP de la machine : {ipMachine}")
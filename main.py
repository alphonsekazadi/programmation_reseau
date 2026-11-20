import socket

nomMachine = socket.gethostname()
print(f"Le nom de la machine : {nomMachine}")

ipMachine = socket.gethostbyname(nomMachine)
print(f"L'IP de la machine : {ipMachine}")

print("")

# Creation du socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.close()
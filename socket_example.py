import socket

socketTest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socketTest)
socketTest.close()
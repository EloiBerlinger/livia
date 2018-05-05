import socket

# Etablishing client connection
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("localhost", 14785))

# Sending messages
message = ""
clientSocket.send(message.encode())

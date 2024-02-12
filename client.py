import socket,time

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)

# Connect to the server's address and port
client_socket.connect(server_address)
print("Connected to server")

# Send a message to the server
username = input("Enter the username: ")
client_socket.send(username.encode())

response = client_socket.recv(1024).decode()
print('Server response:', response)







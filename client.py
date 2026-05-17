import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 65432))

while True:
    message = input("client: ")

    client.send(message.encode())

    data = client.recv(5024)

    print(f"Server: {data.decode()}")


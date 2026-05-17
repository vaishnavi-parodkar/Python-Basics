import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(('0.0.0.0', 65432))


server.listen(1)

print("Listening for connection...")


conn, addr = server.accept()

print(f"Connected by {addr}")

while True:

    data = conn.recv(5024).decode()


    if not data:
        print("Client disconnected")
        break

    if data == "exit":
        print("Disconnecting")
        break

    print(f"Data: {data}")


    datas = input("> ").encode()
    conn.send(datas)


conn.close()
server.close()

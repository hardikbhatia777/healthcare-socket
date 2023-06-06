import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),1234))
s.listen(5)

accounts = {'admin':'1234'}

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    data = clientsocket.recv(1024)
    data = data.decode('utf-8')
    data = eval(data)
    if (data[0] == 1):
        username = data[1]
        password = data[2]
        if(data[1] in accounts):
            confirm = accounts.get(data[1])
            if password == confirm:
                clientsocket.send(bytes("1","utf-8"))
            else:
                clientsocket.send(bytes("2","utf-8"))
        else:
            clientsocket.send(bytes("2","utf-8"))


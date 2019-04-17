import socket
from random import randint

errors = 'Неправильно, повторите ответ. '
ms = 'Правильно. '

HOST = str(input())
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")

conn, addr = server.accept()

print('connected:', addr)

#data = "Hellow \n"
#conn.send(data.encode().upper())

while True:
    x = randint(1, 3)
    y = randint(0, 10)

    answr = ('{} x {} = '.format(x, y))

    print(answr)

    out = answr
    conn.send(out.encode())
    data = conn.recv(2048)
    if not data or data.decode() == "stop":
        break
    print(data.decode())

    if int(data.decode()) != x*y:
    	out = errors
    	conn.send(out.encode().upper())
    	while True:
    		data = conn.recv(2048)
    		if int(data.decode()) == x*y:
    			break
    		out = errors
    		conn.send(out.encode().upper())
    else:
    	out = ms
    	conn.send(out.encode().upper())

conn.close()
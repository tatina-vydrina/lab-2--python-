import socket

message = ''

HOST = str(input())
PORT = 9090


user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user.connect((HOST, PORT))

print('Connected to server')

#data = user.recv(2048)
#print(data.decode())

while message != 'stop':
	data = user.recv(2048)
	print(data.decode())
	message = input('Введите сообщение: \n')
	user.send(message.encode())
user.close()
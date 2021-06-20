import socket
import time

clientSocket = socket.socket()

host = '192.168.56.103'
port = 8888

clientSocket.connect((host,port))

print('\nConnecting to ', host, '....')

time.sleep(1)

response = clientSocket.recv(1024)
print(response.decode('utf-8'))
while True:
	print('*****************')
	print('Welcome to Online Calculator')
	print('*****************')
	print('1. Logarithm         3. Exponential')
	print('2. Square Root       4. Multiplication')
	print('              5. Exit')
	choice = input('\nChoose one number above : ')

	clientSocket.send(choice.encode('utf-8'))

	if int(choice) == 1:
		num = input('\nPlease enter a number to Log : ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Log ',num,':',answer.decode('utf-8'))
	elif int(choice) == 2:
		num = input('\nPlease enter a number to Square Root: ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Square Root ',num,':',answer.decode('utf-8'))
	elif int(choice) == 3:
		num = input('\nPlease enter a number to Exponent: ')
		clientSocket.send(num.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Exponential ',num,':',answer.decode('utf-8'))
	elif int(choice) == 4:
		num = input('\nPlease enter first number : ')
		num2 = input('Please enter second number : ')
		clientSocket.send(num.encode('utf-8'))
		clientSocket.send(num2.encode('utf-8'))
		answer = clientSocket.recv(1024)
		print('Answer for Multiplication ', num, 'x', num2, ':', answer.decode('utf-8'))
	else:
		clientSocket.send(choice.encode('utf-8'))
		print('\nThank You!\n')
		clientSocket.close()
		False
		break
clientSocket.close()

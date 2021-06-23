import socket, time

host = socket.gethostbyname(socket.gethostname())
port = 8080

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print("[Server started]")

#The cycle works while the user is online 
#(it also catches errors, if you wish, you can add a date, but there may be problems with the server) 
while not quit:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		print("["+addr[0]+"]=["+str(addr[1])+"]", end = "")
		print(data.decode('utf-8'))

        #Sender does not receive own messages 
		for client in clients:
			if addr != client:
				s.sendto(data, client)

	except:
		print("\n[Server stopped]")
		quit = True

s.close()

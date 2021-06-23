import socket, threading, time

key = 8194 #random key

shutdown = False
join = False

def receving (name, sock):
	#The loop serves to receive messages and decrypt 
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)

				#Begin Cryptography(XOR)
				decrypt = ""; k = False
				for i in data.decode('utf-8'):
					if i == ':':
						k = True
						decrypt += i
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
				print(decrypt)
				#End

				time.sleep(0.2)
		except:
			pass

host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.0.106", 8080)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rt = threading.Thread(target = receving, args = ("RecvThread", s))
rt.start()

#The loop is used to send messages and encrypt 
while shutdown == False:
	if join == False:
		s.sendto(("["+alias +"] => join chat ").encode('utf-8'), server)
		join = True
	else:
		try:
			message = input("--> ")

			#Begin Cryptography(XOR)
			crypt = ""
			for i in message:
				crypt += chr(ord(i)^key)
			message = crypt
			#End

			if message != "":
				s.sendto(("["+alias + "] :: "+message).encode("utf-8"), server)
			
			time.sleep(0.2)

		except:
			s.sendto(("["+alias +"] <= left chat ").encode('utf-8'), server)
			shutdown = True
rt.join()
s.close()



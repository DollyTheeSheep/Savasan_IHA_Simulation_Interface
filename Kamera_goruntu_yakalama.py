"""
import cv2, imutils, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
host_ip = '192.168.1.5'#  socket.gethostbyname(host_name)
print(host_ip)
port = 9999
message = b'Hello'
client_socket.sendto(message,(host_ip,port))
fps,st,frames_to_count,cnt = (0,0,20,0)
while True:
	packet,_ = client_socket.recvfrom(BUFF_SIZE)
	data = base64.b64decode(packet,' /')
	npdata = np.fromstring(data,dtype=np.uint8)
	frame = cv2.imdecode(npdata,1)
	frame = cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
	cv2.imshow("RECEIVING VIDEO",frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		client_socket.close()
		break
	if cnt == frames_to_count:
		try:
			fps = round(frames_to_count/(time.time()-st))
			st=time.time()
			cnt=0
		except:
			pass
	cnt+=1

"""

# This is server code to send video frames over UDP
import cv2, imutils, socket
import numpy as np
import time
import base64

BUFF_SIZE = 65536
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,BUFF_SIZE)
host_name = socket.gethostname()
print(host_name)
host_ip = '192.168.1.254'#  socket.gethostbyname(host_name)

#host_ip=socket.gethostbyname(host_name)
print(host_ip)
print(host_ip)
port = 9999
socket_address = (host_ip,port)
server_socket.bind(socket_address)
print('Listening at:',socket_address)

vid = cv2.VideoCapture(0) #  replace 'rocket.mp4' with 0 for webcam
fps,st,frames_to_count,cnt = (0,0,20,0)

while True:
	msg,client_addr = server_socket.recvfrom(BUFF_SIZE)
	print('GOT connection from ',client_addr)
	WIDTH=400
	while(vid.isOpened()):
		_,frame = vid.read()
		frame = imutils.resize(frame,width=WIDTH)
		encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,80])
		message = base64.b64encode(buffer)
		server_socket.sendto(message,client_addr)
		frame = cv2.putText(frame,'FPS: '+str(fps),(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
		cv2.imshow('TRANSMITTING VIDEO',frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord('q'):
			server_socket.close()
			break
		if cnt == frames_to_count:
			try:
				fps = round(frames_to_count/(time.time()-st))
				st=time.time()
				cnt=0
			except:
				pass
		cnt+=1


"""
# ----- A simple TCP based server program in Python using send() function -----


import socket

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen

serverSocket.bind(("192.168.1.254", 8080))

serverSocket.listen(3)

# Accept connections
print("while starts")
while (True):
	(clientConnected, clientAddress) = serverSocket.accept()
	print("f1")
	print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

	dataFromClient = clientConnected.recv(1024)

	print(dataFromClient.decode())

	# Send some data back to the client

	clientConnected.send("Hello Client!".encode())

"""
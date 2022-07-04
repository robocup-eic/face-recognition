from custom_socket import CustomSocket
import socket
from ra_face_recognition import RAFaceRecognition
import cv2
import json
import numpy as np
import time

def main() :

	face_reg = RAFaceRecognition("./database")

	server = CustomSocket(socket.gethostname(), 10006)
	server.startServer()
  
	while True :
			conn, addr = server.sock.accept()
			print(f"[CLIENT CONNECTED FROM {addr}]")
      
			while True:
				try :
					data = server.recvMsg(conn)
					# print("data is ==>",data)

					'''
						COMMAND  |  PARAMETER1  |  PARAMETER2
						=====================================
						register |  [image]     |  [name]
						-------------------------------------
						detect   |  [image]     |
					'''

					data = data.split(server.SPLITTER)
					command = data[0].decode()
					print(command)
					print(command == "register")
					if command == "register" :
						name = data[-1].decode()
						print(f"Registering : {name}")
						image = np.frombuffer(b" ".join(data[1:-1]), dtype = np.uint8).reshape(720, 1280, 3)
						print(image)
						status = face_reg.register(name, image)
						print(status)
						server.sendMsg(conn, json.dumps(status, indent = 4))

					if command == "detect" :
						image = np.frombuffer(b" ".join(data[1:]), dtype = np.uint8).reshape(720, 1280, 3)
						names = face_reg.detectFace(image)
						results = {}
						for name in names:
							x, y, w, h = names[name]
							results[name] = {
								"x" : x,
								"y" : y,
								"w" : w,
								"h" : h
							}
						server.sendMsg(conn, json.dumps(results, indent = 4))

				except Exception as e:
						print(e)
						print("Connection Closed")
						break 

if __name__ == '__main__' :
	main()	

	# face_reg = RAFaceRecognition("./database")
	# image = cv2.imread("elon.jpeg")
	# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# status = face_reg.register("test_elon", image)
	# print(status)
	# result = face_reg.detectFace(image)
	# image = cv2.rectangle(image, (result[0], result[1]), (result[0]+result[2],result[1]+result[3]), (255,0,0), 1)
	# cv2.imwrite("elon_detect.png",image[:,:,::-1])
	# print(result)
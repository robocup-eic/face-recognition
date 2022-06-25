from custom_socket import CustomSocket
import socket
from ra_face_recognition import RAFaceRecognition
import cv2
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

					if command == "register" :
						name = data[-1].decode()
						image = np.frombuffer(b" ".join(data[1:-1]), dtype = np.uint8).reshape(720, 1280, 3)
						status = face_reg.register(name, image)
						print(status)

					if command == "detect" :
						image = np.frombuffer(b" ".join(data[1:]), dtype = np.uint8).reshape(720, 1280, 3)
						names = face_reg.detectFace(image)
						print(names)

				except Exception as e:
						print(e)
						print("Connection Closed")
						break 

if __name__ == '__main__' :
	main()	

# face_reg = RAFaceRecognition("./database")
# image = cv2.imread("elon.jpeg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# status = face_reg.register("Elon Musk", image)
# print(status)
# print("="*20)
# result = face_reg.detectFace(image)
# print(result)

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
					print("data is ==>",data)

					'''
						COMMAND  |  PARAMETER1  |  PARAMETER2
						=====================================
						register |  [image]     |  [name]
						-------------------------------------
						detect   |  [image]     |
					'''

					command = data.split()[0]

					if command == "register" :
						image, name = data.split()[1:]
						image = np.frombuffer(image, dtype = np.uint8).reshape(480, 640, 3)
						status = face_reg.register(name, image)
						# print(f"[REGISTER RESPONSE : {"message"}]")
						print(status)

					if command == "detect" :
						image = data.split()[1]
						image = np.frombuffer(image, dtype = np.uint8).reshape(480, 640, 3)
						names = face_reg.detect(image)
						print(names)

				except Exception as e:
						print(e)
						print("Connection Closed")
						break 

# if __name__ == '__main__' :
# 			main()	

face_reg = RAFaceRecognition("./database")
image = cv2.imread("another_elon.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# status = face_reg.register("Elon Musk", image)
# print(status)
# result = face_reg.detectFace(image)
# cv2.imshow("Test", image)
# cv2.waitKey(0)
# face_reg = RAFaceRecognition("./database")
detect_status = face_reg.detectFace(image)
print(detect_status)

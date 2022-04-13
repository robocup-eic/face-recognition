from custom_socket import CustomSocket
import socket
from ra_face_recognition import RAFaceRecognition

def main() :

	face_reg = RAFaceRecognition("./database")

	server = CustomSocket(socket.gethostname(), 10000)
	server.startServer()

	while True :
		conn, addr = server.sock.accept()
		print(f"[CLIENT CONNECTED FROM {addr}]")

		try :
			data = server.recvMsg(conn)

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
				print(f"[REGISTER RESPONSE : {status["message"]}]")

			if command == "detect" :
				image = data.split()[1]
				image = np.frombuffer(image, dtype = np.uint8).reshape(480, 640, 3)
				names = face_reg.detect(image)
				print(names)


if __name__ == "__main__" :
	main()
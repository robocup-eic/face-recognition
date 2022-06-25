from http.client import responses
import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json

# img = cv2.imread("test_pics/test3.jpg")
# print(img.shape)

test_name = 'elon'
image = cv2.imread("another_elon.jpg")
print(image.shape)

host = socket.gethostname()
port = 10006

c = CustomSocket(host,port)
c.clientConnect()

# print(image_with_command)
# data = image_with_command.split("CHAMP"))

cap = cv2.VideoCapture(2)
cap.set(4,720)
cap.set(3,1280)

while cap.isOpened():
	
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue
    
    cv2.imshow('test', frame)
    print(frame.shape)

    print("Send")
    # c.register(image,test_name)

    c.detect(frame)


    if cv2.waitKey(1) == ord("q"):
        cap.release()

cv2.destroyAllWindows()



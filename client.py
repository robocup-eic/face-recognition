from http.client import responses
import socket
import cv2
import numpy as np
import time
from custom_socket import CustomSocket
import json

# img = cv2.imread("test_pics/test3.jpg")
# print(img.shape)

register = b'register '
detect = b'detect '
test_name = b' cena'
image = cv2.imread("cena.jpeg")
print(image.shape)

host = socket.gethostname()
port = 10006

c = CustomSocket(host,port)
c.clientConnect()
print(register)
print(image)
# print(register+(image.tobytes()))
image_with_command = register+image.tobytes()+test_name
print(image_with_command)
while True : 
    print("Send")
    msg = c.req(image_with_command)
    print(msg)
    time.sleep(1)
    break
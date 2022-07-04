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

x = c.register(image, "elonma")
print(x)
# # print(image_with_command)
# # data = image_with_command.split("CHAMP"))

# while True : 
#     print("Send")
#     # c.register(image,test_name)
#     c.detect(image)
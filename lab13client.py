#  clien side : type, encrypt and send ciphertext to server
# Message Sender
import os
from socket import *
from cryptography.fernet import Fernet

host = "127.0.0.1" # set to IP address of target computer
port = 8080
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
key = input("Enter the secret key: ")
f = Fernet(key)


def encrypt(plaintext):
  msg = f.encrypt(plaintext)
  return msg


while True:
  data = str(input("Enter message to send or type 'exit': ")).encode()
  ciphertext = encrypt(data)
  UDPSock.sendto(ciphertext, addr)
  if data == b'exit':
    break
  if data == b'newkey':
    key = input("Enter the secret key: ")
    f = Fernet(key)
    
UDPSock.close()
os._exit(0)
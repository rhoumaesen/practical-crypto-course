from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


from cryptography.exceptions import InvalidSignature

############### RSA Key Generation ##############

private_key= rsa.generate_private_key(
  public_exponent=65537,
  key_size=3072,
  backend=default_backend(), )


public_key=private_key.public_key()

###################################################

########## BoB generates a message and create a signature then send message + signature to Alice

message=b'from bob to alice'
padding_config= padding.PSS(
  mgf=padding.MGF1(hashes.SHA256()),
  salt_length=padding.PSS.MAX_LENGTH)

signature = private_key.sign(
  message,
  padding_config,
  hashes.SHA256())

signed_message={
  'message': list(message),
  'signature': list(signature),
}

outbound_msg_to_alice=json.dumps(signed_message, indent=4)
with open("signaturebob.json", "w") as outfile:
    outfile.write(outbound_msg_to_alice)
print ("===================")

########### Alice receives the json file where message + signature reside abd verifies the signature #################

with open('signaturebob.json', 'r') as openfile: 
    # Reading from json file
    signed_message = json.load(openfile)
  
print(signed_message)

received_msg=bytes(signed_message['message'])
received_signature=bytes(signed_message['signature'])

#padding_config= padding.PSS(
#  mgf=padding.MGF1(hashes.SHA256()),
#  salt_length=padding.PSS.MAX_LENGTH)

public_key=private_key.public_key()
forged_msg=b'from bob to alicee'
try :
  public_key.verify(
    received_signature,
    forged_msg, #received_msg, 
    padding_config,
    hashes.SHA256() )
  print('trust the message')
except InvalidSignature:
  print('Invalid Signature')



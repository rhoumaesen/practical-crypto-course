import rsa

(publickey,privatekey) = rsa.newkeys(1024) # RSA KEY GENRATION with key 

message = input("Enter a message to encrypt with RSA-") # input

#Signing using RSA  with private key
signmsg = rsa.sign(message.encode('ascii'),privatekey,'SHA-1')
print("Signed output is ",signmsg.hex())

#verify with Public Key
verifymsg = rsa.verify(message.encode('ascii'),signmsg,publickey)
if(verifymsg):
    print("Signature is verified")
else:
    print("Signature is not verified")

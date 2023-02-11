import rsa

(publickey,privatekey) = rsa.newkeys(1024) # RSA KEY GENRATION with key sizes- 102420484096
message = input("Enter a message to encrypt with RSA-") # input

#Encryption with Public Key
#ciphertext = rsa.encrypt(message,publickey)
ciphertext = rsa.encrypt(message.encode('ascii'),publickey)
print("Encrypted output is-" ,ciphertext.hex())

#Decryption with private Key
#plaintext = rsa.decrypt(ciphertext,privatekey)
plaintext = rsa.decrypt(ciphertext,privatekey).decode('ascii')
print("Plain text after decryption is- ",plaintext)

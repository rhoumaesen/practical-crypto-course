 

import hashlib
import base64
plaintext_password = b'password'
hashed = hashlib.md5(plaintext_password).digest()
print("binary digest =", hashed)
hhex=hashed.hex()
print("hexadecimal digest =", hhex)
encoded = base64.b64encode(hashed)
print("base64 digest =", encoded)

#import hashlib
#plaintext_password = b'password'
#hashedHEX = #hashlib.md5(plaintext_password).hexdigest()
#print(hashedHEX)


#- - - - - - - - 


print ("----------------------")
print ("----------------------")
print ("----------------------")
print ("----------------------")

import bcrypt

passwd = b's$cret12'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

print(salt)
print(hashed)


print ("----------------------")


#-------------------------
import hashlib

def saltPassword_md5(password):
  salt = b'cHp3'
  hashed = hashlib.md5(salt + password).hexdigest()
  print ("%s:%s" % (salt, hashed)) # Store these
  return hashed
  
plaintext_password = b'Password'
salted_md5 = saltPassword_md5 (plaintext_password)


#------------


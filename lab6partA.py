from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import base64


random_generator = Random.new().read
key = RSA.generate(1024, random_generator)


publickey = key.publickey()
encryptor = PKCS1_OAEP.new(publickey)
encrypted = encryptor.encrypt(b'Hi Bro encrypt this message')
encrptedbase64=base64.b64encode(encrypted)
print('encrypted message:', encrypted)
print()
f = open('encryptionn.txt', 'w')
f.write(str(encrypted))
print(encrptedbase64)
print()
f.close()


f = open('encryptionn.txt', 'r')
message = f.read()
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(encrypted)
print('decrypted : ', decrypted)
f = open('encryptionn.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
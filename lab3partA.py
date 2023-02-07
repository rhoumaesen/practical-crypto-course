import base64
from Crypto.Cipher import DES
from Crypto import Random

iv = Random.get_random_bytes(8)
key='01234567'
key=str.encode(key)

des1 = DES.new(key, DES.MODE_CFB, iv)
des2 = DES.new(key, DES.MODE_CFB, iv)

text = 'hello world'
print("plaintext: ", text)

text=str.encode(text)

cipher_text = des1.encrypt(text)
print("ciphertext :", cipher_text)
cipher_textt=base64.b64encode(cipher_text).decode()
print("encoded base64 ciphertext :", cipher_textt)

decipher_text=des2.decrypt(cipher_text)
#print( decipher_text)
decipher_text=decipher_text.decode("utf-8")
print("recovered :", decipher_text)


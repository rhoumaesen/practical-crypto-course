import os
from Crypto.Cipher import AES
import hashlib
import base64

def encrypt_file(key, in_filename, out_filename=None, chunksize=16*1024):
    
    if not out_filename:
        out_filename = in_filename + '.enc'
    
    iv=os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    #filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            #outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
                chunkd=encryptor.encrypt(chunk)
                chunkd=base64.b64encode(chunkd).decode()
                print(chunkd)

def decrypt_file(key, in_filename, out_filename=None, chunksize=16*1024):
       
    with open(in_filename, 'rb') as infile:        
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
               
                outfile.write(decryptor.decrypt(chunk))
                print(decryptor.decrypt(chunk))

            

password = b'kitty'    
key = hashlib.sha256(password).digest()
print("key: ", key)

encrypt_file(key, 'test.txt', chunksize=16*1024)
print("ciphertext : ")
print("Done")
   
print("plaintext : ")
decrypt_file(key, 'test.txt.enc', 'testdd.txt', chunksize=16*1024)
   
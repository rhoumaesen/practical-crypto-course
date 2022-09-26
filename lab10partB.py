from Crypto.Cipher import AES

key = b"aaaabbbbccccdddd"
cipher = AES.new(key, AES.MODE_ECB)

with open("plane.bmp", "rb") as f:
  byteblock = f.read()
print (len(byteblock))
byteblock_trimmed = byteblock[64:-6]
ciphertext = cipher.encrypt(byteblock_trimmed)
ciphertext = byteblock[0:64] + ciphertext + byteblock[-6:]
with open("e_plane.bmp", "wb") as f:
  f.write(ciphertext)



# decrypt using the reverse process
with open("e_plane.bmp", "rb") as f:
  byteblock = f.read()
  
pad = len(byteblock)%16 * -1
byteblock_trimmed = byteblock[64:pad]
plaintext = cipher.decrypt(byteblock_trimmed)
plaintext = byteblock[0:64] + plaintext + byteblock[pad:]
with open("d_plane.bmp", "wb") as f:
  byteblock = f.write(plaintext)
print ("done")
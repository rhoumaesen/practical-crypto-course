



# - - - - - - -  lect1
import hashlib as hh
hh.sha3_512
x = bytearray(5)
print(x.hex())
a=[1,2,3]
b=a
a.append(4)
print(b)


count=10
while (count < 5):
	print (count)
	count=count+1
else:
  print("count>5")
print("loop finihed")

all_kids = ["Eden", "Hayden", "Kenna"]
for kid in all_kids:
  print (kid)
print(type(all_kids))

def myEnc(plaintext, key):
  print("ciphertext")

myEnc("hello", "KeyError")

def funcc(a,b,c=10,d=100):
  print(a,b,c,d)


funcc(1,2)
funcc(1,2,3,4)
# - - - - --- - - - - - - - 
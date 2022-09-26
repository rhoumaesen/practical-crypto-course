from Crypto.Util.number import *
from Crypto import Random
import Crypto
import gmpy2
import sys

bits=60
msg="Hello how are y"

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

n = p*q
PHI=(p-1)*(q-1)

e=65537
d=(gmpy2.invert(e, PHI))

msgutf=msg.encode('utf-8')
print("the message utf", msgutf)

m=  bytes_to_long(msgutf)

print("the message", m)
c=pow(m,e, n)
res=pow(c,d ,n)

print( "Message=%s\np=%s\nq=%s\nN=%s\ncipher=%s\ndecipher=%s" % (msg,p,q,n,c,(long_to_bytes(res))))
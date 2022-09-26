#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:55:37 2019

@author: root
"""


import hashlib
import base64



data = "secret-message"
print('data=', data)


hash1 = hashlib.sha1(data.encode('utf-8'))

#the fingerprint in bytes
sign1bytes=hash1.digest()
print('sign1 without encoding (means in bytes) = ',sign1bytes)

# the fingerprint  in hexadecimal
signt=hash1.hexdigest()
print('sign1 in hexadeciaml=', signt)

# the fingerprint  in base64
signature1 = base64.b64encode(hash1.digest()).decode()
print("sign1 in base64=",signature1)



print('size of sign1 in bits= ',8*hash1.digest_size)


# here you can explore more hash variants as for sha256 and sha512 
#and repeat the same steps
hash2 = hashlib.sha256(data.encode('utf-8'))
hash3 = hashlib.sha512(data.encode('utf-8'))

signature2 = base64.b64encode(hash2.digest()).decode()
signature3 = base64.b64encode(hash3.digest()).decode()

print("sign2 in base64=",signature2)
print("sig3 in base64=",signature3)

# continue coding here to explore the output of hashlib in diferent output formats
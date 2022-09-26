#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:55:37 2019

@author: root
"""

import hmac
import hashlib

import base64


key="this is the secret key"
print ('key=',key)

data = "secret-message"
print('data=', data)

decodedkey=str.encode(key)
print("key in bytes = ", decodedkey)

#hmac1 = hmac.new(key, data.encode('UTF-8'), hashlib.sha1)
#hmac1 = hmac.new(decodedkey, data, hashlib.sha1)

hmac1 = hmac.new(decodedkey, data.encode('UTF-8'), hashlib.sha1)

#hmac1 in bytes
sign1bytes=hmac1.digest()
print('sign1 without encoding (means in bytes) = ',sign1bytes)

# hmac1 in hexadecimal
signt=hmac1.hexdigest()
print('sign1 in hexadeciaml=', signt)

# hmac1 in base64
signature1 = base64.b64encode(hmac1.digest()).decode()
print("sign1 in base64=",signature1)


#signature1= hmac1.digest()
#signature3 = hmac3.digest()
#signaturex=signature.decode()
#signature1 = hmac1.digest().encode('base64')
#signature2 = hmac3.digest().encode('base64')


print('size of sign1 in bits= ',8*hmac1.digest_size)


# here you can explore more hmac2 variants as for sha256 and sha512 
#and repeat the same steps
hmac2 = hmac.new(decodedkey, data.encode('UTF-8'), hashlib.sha256)
hmac3 = hmac.new(decodedkey, data.encode('UTF-8'), hashlib.sha512)

signature2 = base64.b64encode(hmac2.digest()).decode()
signature3 = base64.b64encode(hmac3.digest()).decode()

print("sign2 in base64=",signature2)
print("sig3 in base64=",signature3)

# continue coding here to explore the output of hmac2 in diferent output formats
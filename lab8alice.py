import hashlib
import hmac
import json



with open('filetoalice.json', 'r') as openfile: 
    # Reading from json file
    authent_msg = json.load(openfile)
  
print(authent_msg)

message=bytes(authent_msg['message'])

hmac_sha256=hmac.new(b'shared_key', digestmod=hashlib.sha256)
hmac_sha256.update(message)
hashv=hmac_sha256.hexdigest()

if hashv ==authent_msg['hash_value']:
  print("message authenricated ! ")


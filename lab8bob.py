import hashlib
import hmac
import json

hmac_sha256=hmac.new(b'shared_key', digestmod=hashlib.sha256)
message=b'message from bob to alice'
hmac_sha256.update(message)
hashv=hmac_sha256.hexdigest()
authent_msg={
  'message' : list(message), 
  'hash_value' : hashv
}
outbound_msg_to_alice=json.dumps(authent_msg, indent=4)
with open("filetoalice.json", "w") as outfile:
    outfile.write(outbound_msg_to_alice)
print ("===================")




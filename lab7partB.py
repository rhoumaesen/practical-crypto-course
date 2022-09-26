import hashlib
m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
print(m.hexdigest())
print(m.digest_size)
print(m.block_size)

#- - - - - - - - 
s=hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
print(s)
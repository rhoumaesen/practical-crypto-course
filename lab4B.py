from cryptography.fernet import Fernet
 # Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
encrypted = f.encrypt(b"This is a test for the new module fernet.")

print(encrypted)
print()
decrypted=f.decrypt(encrypted)
print(decrypted)

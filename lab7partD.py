from cryptosteganography import CryptoSteganography

key = "1111222233334444!"
crypto_steganography = CryptoSteganography(key)
print()

################# transmitter 
print('The program is looking for an image named nebula.png\n')
origfile = "nebula.png"
print('The image with the hidden message will be called mnebula_m..png\n')
modfile = "mnebula_m.png"
secretMsg = ""
message1 = "Sympathy for the favorite nation, facilitating the illusion of an imaginary common "
message2 = "interest in cases where no real common interest exists, and infusing into one the "
message3 = "enmities of the other, betrays the former into a participation in the uarrels nd "
message4 = "wars of the latter without adequate inducement or justification."
secretMsg = secretMsg.join([message1, message2, message3, message4])
crypto_steganography.hide(origfile, modfile, secretMsg)


#### receiver ###############333
secret = crypto_steganography.retrieve(modfile)
print("The secret that is hidden in the file is:\n")
print(secret)
print()

################### wrong receiver #########################
print('Now we will try the wronge secret.\n')
key = "AnotherKey"
crypto_steganography = CryptoSteganography(key)
secret = crypto_steganography.retrieve(modfile)
print('The secret message is: {} \n'.format(secret))
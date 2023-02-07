########################### Q1 Cesar Encryption ################
letters = 'abcdefghijklmnopqrstuvwxyz'


def enc_caesar(n, plaintext):
    result = ''
    for l in plaintext.lower():
        i = (letters.index(l) + n) % 26
        result += letters[i]

    return result.lower()


plaintext = 'hello'
ciphertext = enc_caesar(3, plaintext)
print(ciphertext)

########################### Q2 Cesar Decryption################


def dec_caesar(n, ciphertext):
    result = ''
    for l in ciphertext.lower():
        i = (letters.index(l) - n) % 26
        result += letters[i]

    return result.lower()


cipher = 'khoor'
recovered = dec_caesar(3, cipher)
print(recovered)

######################### Q3 Brute force of Cesar #######################
mystery = 'khoor'
for k in range(len(letters)):
    #print(k)
    decrypted = ''
    for symbol in mystery:
        if symbol in letters:
            num = letters.index(symbol)  # get the number of the symbol
            num = (num - k) % 26
            decrypted += letters[num]

    print('Key #%s: %s' % (k, decrypted))

########################### Q1 Cesar Encryption : improvement assuming that a text can contain ponctuation POINTS like , -, . / ?! etc ################
letters = 'abcdefghijklmnopqrstuvwxyz'


def enc_caesar(n, plaintext):
    result = ''
    for l in plaintext.lower():
        if l in letters:
            i = (letters.index(l) + n) % 26
            result += letters[i]
        else:
            result += l

    return result.lower()


plaintext = 'hello, how are you ? I hope you are fine ! :-)'
ciphertext = enc_caesar(3, plaintext)
print(ciphertext)


################ Question 1 ##################################
def reverseCipher(plaintext):
  ciphertext = ''
  i = len(plaintext) - 1
  while i >= 0:
    ciphertext = ciphertext + plaintext[i]
    i = i - 1
  return ciphertext

  #### encyption
plaintext = "If you want to keep a secret, you must hide it."
ciphertext = reverseCipher (plaintext)
print(ciphertext)

#### Decryption
recovered=reverseCipher (ciphertext)
print(recovered)

############################################################

################ Question 2 ##################################
import getpass
import bcrypt



 
def ask_for_username():
      print("enter the user name would you like to use...")
      username = input()
      return username
 
 

def ask_for_password():
     while True:
      print("What password would you like to create?")
      salt=bcrypt.gensalt()
      p=getpass.getpass()
      inputstr=str.encode(p)      
      hashed_password1 = bcrypt.hashpw(inputstr,salt)
      print(hashed_password1)
      
      print("Please enter the password again...")
      q=getpass.getpass()
      inputstr2=str.encode(q)
      hashed_password2 = bcrypt.hashpw(inputstr,salt)
      print(hashed_password2)
       
      if hashed_password1 == hashed_password2:
        print("Your password is matching...")
        print("Your username, hashed password and salt is stored in testhash.txt file")        
        return hashed_password2, salt
      else:
        print("Your password do not match. Please retry...")

def store_info(username, hashed_pass, salt):
#password_file =open_pass_file()
  with open("testhash.txt", "a" ) as password_file:
    password_file.write(username  + " | " + "".join(map(chr,hashed_pass ))   + " | " + "".join(map(chr, salt )) + "\n" + "\n")
   
    
username = ask_for_username()
hashedPass, salt = ask_for_password()
store_info(username, hashedPass, salt)

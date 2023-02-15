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
 
def ask_for_username():
      print("enter the user name would you like to use...")
      username = input()
      return username
 

def ask_for_password():
     while True:
      print("What password would you like to create?")
     # salt=bcrypt.gensalt()
      p=getpass.getpass()
      inputstr=str.encode(p)      
     # hashed_password1 = bcrypt.hashpw(inputstr,salt)
      print(p)
      
      print("Please enter the password again...")
      q=getpass.getpass()
      inputstr2=str.encode(q)
     # hashed_password2 = bcrypt.hashpw(inputstr,salt)
      print(q)
       
      if p == q:
        print("Your password is matching...")
        print("Your username and password are stored in testhash.txt file")        
        return q
      else:
        print("Your password do not match. Please retry...")

def store_info(username, password):
#password_file =open_pass_file()
  with open("testhash.txt", "a" ) as password_file:
    password_file.write(username  + " | " + password + "\n" + "\n")
   
    
username = ask_for_username()
password = ask_for_password()
store_info(username, password )

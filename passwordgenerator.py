''' secrets module: This module is used for generating random numbers for managing important data such as passwords, account authentication,
security tokens, etc, that are cryptographically strong. 

string module: This module provides string constants that we can use to define the alphabet. 

'''

# import time
import secrets
import string

letters = string.ascii_letters  #The ascii_letters is a concatenation of letters lowercase and uppercase letters.
digits = string.digits  #The digits constant is the string containing the numbers 0 to 9.
special_chars = string.punctuation  #The punctuation constant is the string of all special characters.

alphabet = letters + digits + special_chars  #Now concatenate the above string constants to get the alphabet.

# fix password length
passwd_lenght = 36

# generate a password string
passwd = ''
for i in range(passwd_lenght):
  passwd += ''.join(secrets.choice(alphabet))

print(passwd)

# To repeat above process for the length of the password use loop.
while True:
  passwd = ''
  for i in range(passwd_lenght):
    passwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in passwd)
      and sum(char in digits for char in passwd) >= 2):
    break

print(passwd)
# time.sleep(10)

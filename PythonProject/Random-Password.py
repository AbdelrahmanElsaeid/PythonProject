
#   ascii_lowercase	 ---->     Contain all lowercase letters
#   ascii_uppercase  ---->  	  Contain all uppercase letters
#   ascii_letters	 ---->     Contain both lowercase and uppercase letters
#   digits	         ---->     Contain digits ‘0123456789’.
#   punctuation	     ---->     All special symbols !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
#   printable	     ---->     characters that are considered printable. This is a combination of constants digits, letters, punctuation, and whitespace.


import random
import string

def get_rand_password(length):
    L = string.printable
    new_pas = ''.join(random.choice(L) for i in range(length))
    print("Random Password Is ", new_pas) 

length_pass = int(input("Enter Length : "))
get_rand_password(length_pass)       



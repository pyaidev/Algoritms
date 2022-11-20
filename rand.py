import random
import string

n = int(input("n="))
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(n))
print("Random string of length", 8, 'is:', rand_string)

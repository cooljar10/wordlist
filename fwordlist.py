#!/usr/bin/python
import itertools

#combination words more input in this more time it will take to finish

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-='

#Length of the password remember the bigger it is the more space

n = 5

#where password.txt is where you can change the name of The Doc
 
for xs in itertools.product (chars, repeat=n) :
    with open ("password.txt", "a+") as wordlist:
         wordlist.write(str(''.join(xs)) + '\n')
    print(' '.join(xs))



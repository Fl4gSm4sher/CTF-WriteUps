#!/usr/bin/python2

# CRYPTO - EASY
# A Prime Hash Candidate

# Based on the fact that database contains the hash of the password and not the actual password
# So the vulnerability is that what if another entirely differrent password will giva exactly the same hash

# **************************************************** #
# PASSWD = "59784015375233083673486266" ## the hash of the actual password

# def hash(data):                       ## A weak hash generator
#     out = 0
#     for c in data:
#         out *= 31                     #/*********************************************************
#         out += ord(c)                 # * let n = len(data), o(i) is ord(data[i]),              *
#     return str(out)                   # * a^b is a to the power of b then the final out will be *
#                                       # * out = o(1)*(31^(n-1)) + o(2)*(31^(n-2)) + ... + o(n)  *
#                                       # * So every time when divided, hashed_passwd with 31     *
#                                       # * the remainder is the last term left {o(n)}.           *
#                                       # *********************************************************/
# **************************************************** #

hashed_passwd = 59784015375233083673486266
passwd_arr = []
while(hashed_passwd):
	possible_remainder = hashed_passwd % 31
	also_possible_remainder = possible_remainder + 62
	passwd_arr.append(chr(also_possible_remainder))
	hashed_passwd = (hashed_passwd - also_possible_remainder)/31
another_passwd_with_same_hash = ''.join(passwd_arr[::-1])
print(another_passwd_with_same_hash) ## use this password in nc to get the flag

# Or alternatively find the hash of "another_passwd_with_same_hash" 
# by declaring "data" with this in the server.py script :)

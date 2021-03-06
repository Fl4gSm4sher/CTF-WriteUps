# by printing the binary of first five characters, and
# comparing it with the binary of 's','d','c','t','f'
# we get to know that there is an extra '0' at the end of every byte
# also the challenge description gives away this hint

from os.path import dirname

flag = ''

with open(dirname(__file__) + "/../flag.dat", "rb") as f:
    # CHUNKSIZE = 1
    bytes_read = f.read()
    while bytes_read:
        for b in bytes_read:
            #--can-do-something-with-the-byte--#
            # note: b is of int type
            # print(type(b)) --> int type
            # print(bin(b)[2:],bin(b)[:-1]) 
            flag += chr(int(bin(b)[:-1],2)) # removes the tailing '0'
        bytes_read = f.read()

print(flag)
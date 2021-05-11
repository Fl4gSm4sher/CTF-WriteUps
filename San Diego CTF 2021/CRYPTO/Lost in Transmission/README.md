# Lost in Transmission
`CRYPTO - EASY`
> I had my friend send me the flag, but it seems a bit...off.<br>
> Flag Message [flag.dat](https://github.com/Fl4gSm4sher/CTF-WriteUps/raw/main/San%20Diego%20CTF%202021/CRYPTO/Lost%20in%20Transmission/flag.dat)


## Explanation
[byte-manupulation.py](https://github.com/Fl4gSm4sher/CTF-WriteUps/raw/main/San%20Diego%20CTF%202021/CRYPTO/Lost%20in%20Transmission/byte-manupulation.py):
```py
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
```
**NOTE:** To download challenge files: 
```bash
curl -O <link-of-the-file>
```
Challenge Solved by:<br>
~[CyberCitizen01](https://ctftime.org/user/107482)

Writeup Author:<br>
~[CyberCitizen01](https://ctftime.org/user/107482)

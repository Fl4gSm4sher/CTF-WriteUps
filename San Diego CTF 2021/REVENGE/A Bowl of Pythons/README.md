# A Bowl of Pythons
`REVENGE - EASY`
> A bowl of spaghetti is nice. What about a bowl of pythons?<br>
> [chal.py](https://raw.githubusercontent.com/Fl4gSm4sher/CTF-WriteUps/main/San%20Diego%20CTF%202021/REVENGE/A%20Bowl%20of%20Pythons/chal.py)

## Explanation
[chall-sol.py](https://raw.githubusercontent.com/Fl4gSm4sher/CTF-WriteUps/main/San%20Diego%20CTF%202021/REVENGE/A%20Bowl%20of%20Pythons/chall-sol.py)

```py
   1  #! /usr/bin/env python3
   2  #/******************************
   3  ## It requires the knowledge of:
   4  ## WHat is lambda ?, What is eval ?
   5  ## Fibonacci series, and how to encode strings, decode bytes, encode strings from hex
   6  
   7  ## lambda: https://www.w3schools.com/python/python_lambda.asp
   8  ## eval: https://realpython.com/python-eval-function/
   9  ## Fibonacci series: https://www.youtube.com/watch?v=ZC-d4dKTyKw
  10  ## string encoding, bytes decoding ... : https://stackoverflow.com/questions/14472650/python-3-encode-decode-vs-bytes-str and ...
  11  #******************************/
  12  
  13  
  14  #//*********chal.py**************
  15  # #! /usr/bin/env python3
  16  # FLAG = 'sdctf{a_v3ry_s3cur3_w4y_t0_st0r3_ur_FLAG}' # lol
  17  
  18  # a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1) #fibonacci series generator by recursion
  19  
  20  # b = lambda x: bytes.fromhex(x).decode()                           # to convert string of hex-->bytes-->string
  21                                                                      # eg: b('414243') will return 'ABC'
  22                                                                      # 'A' in hex is '\x41', 'B' in hex is '\x42' 
  23  
  24  # h = eval(b('7072696e74'))                                         # b('7072696e74') will return 'print'
  25                                                                      # and eval('print') will return an reference to print function
  26                                                                      # so h('hello world') will print 'hello world' as the output
  27  
  28  # def d():                                                          # A function to print 'Incorrect flag! You need to hack deeper...' i.e. line 30
  29  #                                                                   # and exit with status code 1 i.e. line 31
  30  #     h(b('496e636f727265637420666c61672120596f75206e65656420746f206861636b206465657065722e2e2e'))
  31  #     eval(b('5f5f696d706f72745f5f282273797322292e65786974283129'))
  32  #     h(FLAG)                                                       # never gets executed :)
  33  
  34  # def e(f):                                                         # the main function to get the flag!!    
  35  #     h("Welcome to SDCTF's the first Reverse Engineering challenge.") #prints the welcome prompt at the begining
  36  #     c = input("Input the correct flag: ")
  37  #     if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])): # checks if the first six characters of given input is 'sdctf{'
  38  #         d()
  39  #     if c[int(chr(45) + chr(49))] != chr(125):                     # checks if the last character of given input is '}'
  40  #         d()
  41  #     g = c[6:-1].encode()                                          # The part between '{' and '}'
  42  #
  43  #                                                                      #/*******************************************************************************
  44  #     if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:  #* This is where each character of trimed input is xored with the corresponding *
  45  #         d()                                                          #* term of the (fibonacci series & 0xff) # & --> bitwise and,                   *
  46  #                                                                      #* to compare with f i.e. the argument passed at line 52                        *
  47  #                                                                      #* Note a(i) & 0xff is same as a(i) until a(i)<256                              *
  48  #                                                                      #* But after some iterations it will not be the same                            *
  49  #     h(b('4e696365206a6f622e20596f7520676f742074686520636f727265637420666c616721'))                                                                   *
  50  #                                                                      #* line 49 hints that the flag is hidden in line 44                             *
  51  #                                                                      #*******************************************************************************/
  52  # if __name__ == "__main__":
  53  #     e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
  54  # else:
  55  #     eval(b('5f5f696d706f72745f5f282273797322292e65786974283029')) # exit with status code 1
  56  #******************************//
  57  
  58  
  59  
  60  a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)
  61  ## So finally, reversing this line :
  62  ## bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) )
  63  ## will give the flag!!
  64  flag = b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4'
  65  ans = ''
  66  for i in range(len(flag)):
  67      ans += (chr(flag[i] ^ (a(i) & 0xff)))
  68  print('sdctf{'+ans+'}')
  69
```

**NOTE:** To download challenge files: 
```bash
curl -O <link-of-the-file>
```
<br>

Challenge Solved by:<br>
~[CyberCitizen01](https://ctftime.org/user/107482)

Writeup Author:<br>
~[CyberCitizen01](https://ctftime.org/user/107482)

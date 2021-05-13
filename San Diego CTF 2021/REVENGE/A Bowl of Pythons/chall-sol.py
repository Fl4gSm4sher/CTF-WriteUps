#! /usr/bin/env python3
#/******************************
## It requires the knowledge of:
## WHat is lambda ?, What is eval ?
## Fibonacci series, and how to encode strings, decode bytes, encode strings from hex

## lambda: https://www.w3schools.com/python/python_lambda.asp
## eval: https://realpython.com/python-eval-function/
## Fibonacci series: https://www.youtube.com/watch?v=ZC-d4dKTyKw
## string encoding, bytes decoding ... : https://stackoverflow.com/questions/14472650/python-3-encode-decode-vs-bytes-str and ...
#******************************/


#//*********chal.py**************
# #! /usr/bin/env python3
# FLAG = 'sdctf{a_v3ry_s3cur3_w4y_t0_st0r3_ur_FLAG}' # lol

# a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1) #fibonacci series generator by recursion

# b = lambda x: bytes.fromhex(x).decode()                           # to convert string of hex-->bytes-->string
                                                                    # eg: b('414243') will return 'ABC'
                                                                    # 'A' in hex is '\x41', 'B' in hex is '\x42' 

# h = eval(b('7072696e74'))                                         # b('7072696e74') will return 'print'
                                                                    # and eval('print') will return an reference to print function
                                                                    # so h('hello world') will print 'hello world' as the output

# def d():                                                          # A function to print 'Incorrect flag! You need to hack deeper...' i.e. line 30
#                                                                   # and exit with status code 1 i.e. line 31
#     h(b('496e636f727265637420666c61672120596f75206e65656420746f206861636b206465657065722e2e2e'))
#     eval(b('5f5f696d706f72745f5f282273797322292e65786974283129'))
#     h(FLAG)                                                       # never gets executed :)

# def e(f):                                                         # the main function to get the flag!!    
#     h("Welcome to SDCTF's the first Reverse Engineering challenge.") #prints the welcome prompt at the begining
#     c = input("Input the correct flag: ")
#     if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])): # checks if the first six characters of given input is 'sdctf{'
#         d()
#     if c[int(chr(45) + chr(49))] != chr(125):                     # checks if the last character of given input is '}'
#         d()
#     g = c[6:-1].encode()                                          # The part between '{' and '}'
#
#                                                                      #/*******************************************************************************
#     if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:  #* This is where each character of trimed input is xored with the corresponding *
#         d()                                                          #* term of the (fibonacci series & 0xff) # & --> bitwise and,                   *
#                                                                      #* to compare with f i.e. the argument passed at line 52                        *
#                                                                      #* Note a(i) & 0xff is same as a(i) until a(i)<256                              *
#                                                                      #* But after some iterations it will not be the same                            *
#     h(b('4e696365206a6f622e20596f7520676f742074686520636f727265637420666c616721'))                                                                   *
#                                                                      #* line 49 hints that the flag is hidden in line 44                             *
#                                                                      #*******************************************************************************/
# if __name__ == "__main__":
#     e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
# else:
#     eval(b('5f5f696d706f72745f5f282273797322292e65786974283029')) # exit with status code 1
#******************************//



a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)
## So finally, reversing this line :
## bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) )
## will give the flag!!
flag = b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4'
ans = ''
for i in range(len(flag)):
    ans += (chr(flag[i] ^ (a(i) & 0xff)))
print('sdctf{'+ans+'}')


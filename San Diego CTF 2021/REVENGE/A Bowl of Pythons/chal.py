#! /usr/bin/env python3
FLAG = 'sdctf{a_v3ry_s3cur3_w4y_t0_st0r3_ur_FLAG}' # lol

a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)

b = lambda x: bytes.fromhex(x).decode()

h = eval(b('7072696e74'))

def d():
    h(b('496e636f727265637420666c61672120596f75206e65656420746f206861636b206465657065722e2e2e'))
    eval(b('5f5f696d706f72745f5f282273797322292e65786974283129'))
    h(FLAG)

def e(f):
    h("Welcome to SDCTF's the first Reverse Engineering challenge.")
    c = input("Input the correct flag: ")
    if c[:6].encode().hex() != '{2}3{0}{1}{0}3{2}{1}{0}{0}{2}b'.format(*map(str, [6, 4, 7])):
        d()
    if c[int(chr(45) + chr(49))] != chr(125):
        d()
    g = c[6:-1].encode()
    if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:
        d()
    h(b('4e696365206a6f622e20596f7520676f742074686520636f727265637420666c616721'))

if __name__ == "__main__":
    e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
else:
    eval(b('5f5f696d706f72745f5f282273797322292e65786974283029'))

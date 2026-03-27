def create_matrix(key):
    key = key.upper().replace("J","I")
    s = ""
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in s and c.isalpha():
            s += c
    return [s[i:i+5] for i in range(0,25,5)]

def find(m, ch):
    for i in range(5):
        for j in range(5):
            if m[i][j] == ch:
                return i, j

def prepare(t):
    t = t.upper().replace("J","I").replace(" ","")
    res, i = "", 0
    while i < len(t):
        a = t[i]
        b = t[i+1] if i+1 < len(t) else "X"
        if a == b:
            res += a + "X"
            i += 1
        else:
            res += a + b
            i += 2
    return res

def encrypt(t, m):
    t = prepare(t)
    c = ""
    for i in range(0,len(t),2):
        a,b = t[i],t[i+1]
        r1,c1 = find(m,a)
        r2,c2 = find(m,b)
        if r1==r2:
            c += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
        elif c1==c2:
            c += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
        else:
            c += m[r1][c2] + m[r2][c1]
    return c

# Example
m = create_matrix("KEY")
print(encrypt("HELLO", m))
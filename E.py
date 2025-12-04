t = int(input())
MOD = 10**9+7
fact = [1,1,2]
def binexp(base: int, exp: int, mod: int = MOD) -> int:
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:  
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1  
    return result

def inv(x):
    return binexp(x, MOD - 2, MOD)

def precompute():
    for i in range(3,10**6+5):
        fact.append((fact[i-1]*i)%MOD)
precompute()
# print(fact)

for i in range(t):
    n,r = map(int,input().split())
    if r == 1 :
        print(n)
    elif r == n-1:
        print(fact[n])
    else:
        print((fact[n]*inv(fact[n-r]))%MOD)
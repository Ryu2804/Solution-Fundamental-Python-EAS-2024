n = int(input())
d = []

def find_allsub(s):
    last = 0
    awa = 0
    sv = []
    for i,c in enumerate(s):
        if len(sv)<3:
            sv.append(c)
        else:
            # print(sv)
            if "".join(sv) == "awa":
                awa+=1
                last = i 
            sv.pop(0)
            sv.append(c)
    if "".join(sv) == "awa":
        awa += 1
        last = i+1 
    return awa,last

def calc_a(s):
    cnt=0
    for el in s:
        if el == 'a':
            cnt+=1
    return cnt

for i in range(n):
    nick,key = input().split()
    awa, last = find_allsub(key)
    clc = calc_a(key[last:])
    ln = len(key)
    d.append([awa,clc,ln,-i,nick])
d.sort()
for x in d[::-1]:
    print(x[4])
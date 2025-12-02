n,d = map(int,input().split())
baris = list(map(int,input().split()))
baris.sort()
sv = []

for i in range(n):
    if len(sv) == 0 or sv[-1]+d <= baris[i]:
        sv.append(baris[i])
print(len(sv))
print(" ".join(map(str,sv)))
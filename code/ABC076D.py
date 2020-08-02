"""
ABC076_D AtCoderExpress
"""
N = int(input())
T = list(map(int,input().split()))
V = list(map(int,input().split()))

T = T + [0]
V = [0] + V + [0]

SumT = [0] * (N+2)
for i in range(N+1):
    SumT[i+1] = SumT[i] + T[i]
Tmax = SumT[N+1]

#print(SumT)
#print(V)
area = 0
prev_v = 0
i = 0.5
j = 1
while i <= Tmax:
    if i > SumT[j]:
        j += 1
    # FIXIT ここ直後の区間の制限値しか見てないけど、全区間のしばりが必要。order Jかかるけどしょうがない
    now_v = V[j]
    for k in range(N+2):
        if j == k:
            continue
        else:
            now_v = min(now_v, (SumT[j] - i) + V[j+1]))
    area += (prev_v + now_v) * 0.25
    #print(i,now_v)
    prev_v = now_v
    i += 0.5
    
print(area)
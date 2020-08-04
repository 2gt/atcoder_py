N,M = list(map(int, input().split()))
A = []

B = [0] * N
for _ in range(M):
  a,b = list(map(int, input().split()))
  a -= 1
  b -= 1
  B[a] += 2**b


## トポロジカルソートの数え上げ
## bitDPを使う
#https://ikatakos.com/pot/programming_algorithm/graph_theory/topological_sort
# B[n] = ノードnからの流出先ノードの集合のbitフラグ
dp = [0] * (1 << N)
dp[0] = 1
# ノードIDと対応するビット位置は繰り返し求めるので事前計算しておく
jbs = [(j, 1 << j) for j in range(N)]

for i in range(1 << N):
  for j, jb in jbs:
    if (i & jb) == 0 and (i & B[j]) == 0:
      dp[i | jb] += dp[i]

#print(dp)
print(dp[-1])
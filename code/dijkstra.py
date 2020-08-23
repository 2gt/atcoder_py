# gigacode_2019_e
# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_e
# TLEします

import heapq
N, L = map(int, input().split())
VS, DS = map(int, input().split())
A = [(0, VS, DS), (L, 0, 0)]
G = [[] for _ in range(N+2)]

for i in range(N):
  x, v, d = map(int, input().split())
  A.append((x, v, d))

A.sort()
for i in range(N+2):
  x1, v1, d1 = A[i]
  for j in range(i+1, N+2):
    x2, v2, d2 = A[j]
    if x2-x1 <= d1:
      # reachable
      # print(x1,x2, v1,d1,i,j)
      G[i].append((j, (x2-x1)/v1))

"""
print(A)
for g in G:
  print(g)
"""

# dij
h = []
seen = [False] * (N+2)
heapq.heappush(h, (0, 0))
ans = -1
while h:
  dist, now = heapq.heappop(h)
  if seen[now]:
    continue
  seen[now] = True
  if now == N+1:
    ans = dist
    break
  for nxt, ndis in G[now]:
    if seen[nxt]:
      continue
    heapq.heappush(h, (dist + ndis, nxt))

print(format(ans, ".21f") if ans > 0 else "impossible")

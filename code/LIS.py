# ABC134_E

from bisect import bisect_left, bisect_right
N = int(input())
seq = [0] * N
for i in range(N):
  # この問題は広義単調減少列を求めるので、マイナスをかけている
  seq[i] = (-1) * int(input())

# Nに大きさ、AにINPUTの配列を渡すと、LISの配列が返ってくる（はず）
# bisect_right/leftの使い分けがポイントっぽい。バグ実装が多かったので次回以降はこちらを使いたい
# http://even-eko.hatenablog.com/entry/2013/09/05/215236 のPython実装版。
def getLIS(_N,a):
  INF = 1e18
  MaxP = _N+10
  dp = [INF for _ in range(MaxP)]
  for i in range(_N):
    dp[bisect_right(dp,a[i])] = a[i]

  #print(dp[:10])
  return dp[:bisect_left(dp, INF)]

LIS2 = getLIS(N,seq)

print(len(LIS2))
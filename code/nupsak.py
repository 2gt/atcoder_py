## ABC032_D
N, W = map(int, input().split())
ITEM = []
vmax, wmax = 0,0
for _ in range(N):
  v,w = map(int, input().split())
  ITEM.append((v,w))
  vmax = max(vmax,v)
  wmax = max(wmax,w)

INF = 10**18
def solve1():
  #dp[i][v] i個めまで選んで、価値Vを実現するための最小の重量
  # TLEしたらiを消す。
  dp = [INF] * (vmax*N+1)
  dp[0] = 0
  for i in range(1,N+1):
    v1,w1 = ITEM[i-1]
    # dp[i]消すなら、vは大きい方から探索する
    for v in range(vmax*i,-1,-1):
      if v-v1>=0:
        dp[v] = min(dp[v], dp[v-v1]+w1)
  ret = 0
  for i in range(len(dp)):
    if dp[i] <= W:
      ret = max(ret, i)
  #print(dp[:30])
  return ret
    
def solve2():
  #dp[i][w] i個目までを選んで、重さW以下で実現できる最大の価値
  # TLEしたらiを消す。
  dp = [0] * (wmax*N+1)
  dp[0] = 0
  for i in range(1,N+1):
    v1,w1 = ITEM[i-1]
    # dp[i]消すなら、wは大きい方から探索する
    for w in range(wmax*i,-1,-1):
      if w-w1>=0:
        dp[w] = max(dp[w], dp[w-w1]+v1)
  ret = max(dp[:W+1])
  
  #print(dp[2900:2930])
  return ret

def solve3():
  # 半分全列挙。。
  ITEM1,ITEM2 = ITEM[:N//2], ITEM[N//2:]
  #print(ITEM1)
  #print(ITEM2)
  def zenrekkyo(I):
    NI = len(I)
    ret = []
    # bitDP
    for i in range(2**NI):
      v,w = 0,0
      for j in range(NI):
        if i%2==1:
          v1,w1 = I[j]
          v += v1
          w += w1
        i = i // 2
      ret.append([w,v])
    return ret
  ZEN1 = zenrekkyo(ITEM[:N//2])
  ZEN2 = zenrekkyo(ITEM[N//2:])
  ZEN1.sort()
  ZEN2.sort()
   
  # 単調増加に変換しておく。W以下で得られる最大価値Vにしておく、と言うこと。
  for i in range(1,len(ZEN2)):
    ZEN2[i][1] = max(ZEN2[i-1][1], ZEN2[i][1])
  #print(ZEN2)
  idx2 = len(ZEN2)-1
  ret = 0
  #print(len(ZEN1))
  for w1,v1 in ZEN1:
    if w1 <= W:
      ret = max(ret, v1)
    while idx2 < len(ZEN2) and idx2 >= 0:
      w2,v2 = ZEN2[idx2]
      if w1+w2 <= W:
        #print(w1,w2,v1,v2,ret)
        ret = max(ret, v1+v2)
        break
      else:
        idx2 -= 1    
  return ret

# 3patternのナップサックをかく！
if vmax <= 1000:
  ans = solve1()
elif wmax <= 1000:
  ans = solve2()
else:
  ans = solve3()
  
print(ans)
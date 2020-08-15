

# gigacode_2019_d
# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d

H,W,K,V = map(int, input().split())
A = []
for _ in range(H):
  A.append(list(map(int, input().split())))

SA = [[0 for i in range(W+1)] for i in range(H+1)]
for i in range(H):
  for j in range(W):
    SA[i+1][j+1] = SA[i+1][j] + SA[i][j+1] - SA[i][j] + A[i][j]

#for a in SA:
#  print(a)

def solve(a,b):
  #print(a,b)
  # (1,1) (a+1,b+1) の四角形から
  # (H-a,W-b) (H,W)　の四角形までサーチすれば良い
  ###### ここを正確に実行すること。minus oneのところ。
  ### (p,q) (x,y)のとき、 S[x][y] - S[x][q-1] - S[p-1][y] + S[p-1][q-1].
  ### この例だと、Aは0-indexedだが、SAは1-indexedとして扱っている。
  for i in range(1,H-a+1):
    for j in range(1,W-b+1):
      wk = SA[i+a][j+b] - SA[i-1][j+b] - SA[i+a][j-1] + SA[i-1][j-1]
      #print(wk, (a+1)*(b+1)*K, V)
      if wk + (a+1)*(b+1)*K <= V:
        return True
  #print(a,b)
  return False

ans = 0
for i in range(0,H):
  # Hを固定した時、Wを変えながらやって、失敗したら次のHに進む
  for j in range(0,W):
    if solve(i,j):
      ans = max(ans, (i+1)*(j+1))
    else:
      break

print(ans)
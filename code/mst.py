# minimum_spanning_tree
# 最小全域木
# https://note.nkmk.me/python-scipy-minimum-spanning-tree/

#ABC065_D
# この問題だとTLEするので注意。。。
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix

N = int(input())
P = []
for _ in range(N):
  x,y = map(int, input().split())
  P.append((x,y))

D = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(N):
    a,b = P[i]
    c,d = P[j]
    D[i][j] = min(abs(a-c), abs(b-d))

mst = minimum_spanning_tree(D)
print(int(mst.sum()))

######
# #TLEしない版
# 解説の通りでN**2 Edgeを貼っちゃダメ。X,Y座標で各々ソートすれば2N本くらいにできる
# かつ疎行列を使ってcsgraphを作ること。ここはライブラリの癖だが重要
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix, coo_matrix, lil_matrix
from operator import itemgetter

N = int(input())
P = []
for i in range(N):
  x,y = map(int, input().split())
  P.append((x,y,i))

#print(csr_matrix((data, (row, col))).toarray())

data = []
row = []
col = []

P.sort() 
# 覚えておく
D = {}
for i in range(N-1):
  a,b,p = P[i]
  c,d,q = P[i+1]
  cost = min(abs(a-c), abs(b-d))
  data.append(cost)
  row.append(p)
  col.append(q)
  data.append(cost)
  row.append(q)
  col.append(p)
  D[(p,q)] = cost
  D[(q,p)] = cost

P.sort(key=itemgetter(1))
for i in range(N-1):
  a,b,p = P[i]
  c,d,q = P[i+1]
  if (p,q) in D:
    # もしもX座標側の時にAppendしてるのと同じEdgeだったらやらない。重複Edgeの扱いが微妙そうなので注意！
    continue
  cost = min(abs(a-c), abs(b-d))
  data.append(cost)
  row.append(p)
  col.append(q)
  data.append(cost)
  row.append(q)
  col.append(p)
  D[(p,q)] = cost
  D[(q,p)] = cost

coo = coo_matrix((data, (row, col)), (N, N))
mst = minimum_spanning_tree(coo)
print(int(mst.sum()))
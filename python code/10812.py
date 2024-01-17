n, m=map(int, input().split())
box = [0 for i in range(0,n)]

for _ in range(m):
    i, j, z = map(int, input().split())
    for o in range(i-1,j):
      box[o] = z
      

for b in box:
  print(b, end=' ')

#암호조건
#한개의 모음, 최소 2개의 자음
#암호 오름차순
from itertools import combinations

L, C = map(int, input().split())
code = input().split()
alpha = combinations(sorted(code), L)

answer = []
for i in alpha:
  bc, ae = 0, 0
  for j in i:
    if j in 'aeiou':
      ae += 1
    else:
      bc += 1

  if ae >= 1 and bc >= 2:
    print(''.join(i))
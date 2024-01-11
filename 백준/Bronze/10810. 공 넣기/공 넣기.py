import sys

N, M = map(int, sys.stdin.readline().split())
a = []

for _ in range(N):
    a.append(0)

for _ in range(M):
    num1, num2, ball_num = map(int, sys.stdin.readline().split())
    for i in range(num1, num2 + 1):
        a[i - 1] = ball_num

for i3 in range(N):
    print(a[i3], end=' ')
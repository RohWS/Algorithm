H, M, S = map(int, input().split())
N = int(input())
T = (3600 * H) + (60 * M) + (S) + N
while T >= 86400:
  T = T - 86400
H = T//3600
M = (T - (H * 3600))//60
S = (T - (H * 3600) - (60 * M))
print(H, M, S,"\n")
# print(N)
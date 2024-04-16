N = int(input())
fo = list(map(int, input().split()))
dp = [1] * N
for i in range(N):
  for j in range(i):
    if fo[i] > fo[j]:
      dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
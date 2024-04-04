import sys
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
line1 = []
graph = []
for i in range(N):
  graph.append([0] * N)
for i2 in range(M):
  line1.append(list(map(int, input().split())))
#그래프로 구현
for i3 in range(M):
  graph[line1[i3][0] - 1][line1[i3][1] - 1] = 1
  graph[line1[i3][1] - 1][line1[i3][0] - 1] = 1

visited = [0] * N


def dfs(v, label):
  visited[v] = label
  for u in range(N):
    if graph[v][u] == 1 and visited[u] == False:
      dfs(u, label)


cnt = 0
for i4 in range(N):
  if (visited[i4] == False):
    cnt += 1
    dfs(i4, cnt)

print(cnt)
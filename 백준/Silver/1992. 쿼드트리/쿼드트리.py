import sys
input = sys.stdin.readline

n = int(input())
quard = [list(map(int, input().strip())) for _ in range(n)]
def dfs(x, y, n):
    check = quard[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != quard[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end = '')
        dfs(x, y, n//2) 
        dfs(x, y+n//2, n//2)
        dfs(x+n//2, y, n//2)
        dfs(x+n//2, y+n//2, n//2)
        print(")", end = '')

    elif check == 1:
        print(1, end = '')
    else:
        print(0, end = '')

dfs(0, 0, n)
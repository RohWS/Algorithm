import sys

N = int(input())
members = [sys.stdin.readline().strip().split() for _ in range(N)]
members.sort(key=lambda x: int(x[0]))
for member in members:
  sys.stdout.write(f"{' '.join(member)}\n")
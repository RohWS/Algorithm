T = int(input())
result = 1000 - T

coin = 0

money = [500, 100, 50, 10, 5, 1]

for i in money:
  if result == 0:
    break

  coin += result // i
  result %= i

print(coin)
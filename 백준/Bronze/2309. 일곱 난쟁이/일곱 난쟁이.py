T = [int(input()) for _ in range(9)]

S = list(T) #copy
sum_S = sum(S) # > 100
sub_S = int(sum_S - 100)

a = 0
while a < 9:
    S = list(T)
    no_drf2 = int(sub_S - S[a])
    S.remove(S[a])
    if no_drf2 in S:
        S.remove(no_drf2)
        break
    else:
        a += 1

S.sort()
for i in range(len(S)):
    print(S[i])
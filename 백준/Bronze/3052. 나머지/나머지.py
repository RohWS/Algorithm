#set, for, dic 을 이용해서 중복값 제거
# 1. set
b = []
for i in range(10):
  a = int(input())
  a = a%42
  b.append(a)
set_b = set(b)
print(len(set_b))
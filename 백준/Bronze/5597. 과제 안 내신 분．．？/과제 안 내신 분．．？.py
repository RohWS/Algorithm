#list.remove 를 이용한 원소 삭제
a = []
for i in range(30):
  a.append(i+1)
for _ in range(28):
  b = int(input()) # int 넣어서 정수형으로 변환
  a.remove(b)
#첫줄에는 작은 숫자 두번째는 큰 숫자
for i2 in range(2):
  print(a[i2])
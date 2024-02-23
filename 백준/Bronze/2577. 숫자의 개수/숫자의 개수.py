N1 = int(input())
N2 = int(input())
N3 = int(input())
NUM = N1 * N2 * N3
NUM_list = list(map(int, str(NUM)))
for i in range(10):
    print(NUM_list.count(i))

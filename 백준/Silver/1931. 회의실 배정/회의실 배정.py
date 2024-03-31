N = int(input())
meeting_list = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting_list.append((start, end))

meeting_list.sort(key=lambda x: (x[1], x[0]))

count = 1
final_end = meeting_list[0][1]
len_meeting_list = len(meeting_list)
for i in range(1, len_meeting_list):
    start_time = meeting_list[i][0]
    if start_time >= final_end:
        count += 1
        final_end = meeting_list[i][1]

print(count)

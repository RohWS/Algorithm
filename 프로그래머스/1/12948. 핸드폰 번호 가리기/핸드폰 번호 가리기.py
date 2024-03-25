def solution(phone_number):
    a = []
    for i in range(len(phone_number)-4):
        a.append("*")
    for i in range(len(phone_number)-4, len(phone_number)):
        a.append(phone_number[i])
    return ''.join(a)
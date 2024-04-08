def solution(s):
    if len(s) == 4 or len(s) == 6: 
        for i in range(len(s)):
            if 90 >= ord(s[i]) >= 65 or 122 >= ord(s[i]) >= 97:
                answer = False
                break
            else:
                answer = True
    else:
        answer = False
    return answer
# 프로그래머스 | 최대공약수와 최소공배수
def solution(n, m):
    gcd = 0
    lcm = 0
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    lcm = ( n * m) // gcd
    return [gcd, lcm]
def recursion(s, l, r):
    if l >= r: return 1,l+1
    elif s[l] != s[r]: return 0,l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))
T = int(input())

for _ in range(T):
    s = input()
    # l = 0
    # r = 0
    print(isPalindrome(s)[0], isPalindrome(s)[1])
    
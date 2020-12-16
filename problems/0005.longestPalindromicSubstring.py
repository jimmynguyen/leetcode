# https://leetcode.com/problems/longest-palindromic-substring/
import util


def longestPalindromicSubstring_bruteForce(s):
    l = 1
    r = s[0]
    n = len(s)
    i = 0
    while i < n:
        j = i+l
        t = s[i:j-1]
        while j < n+1:
            t += s[j-1]
            if t == t[::-1]:
                r = t
                l = j-i
            j += 1
        i += 1
    return r


def longestPalindromicSubstring_longestCommonSubstring(s):
    t = s[::-1]
    n = len(s)
    l = [[0] * n for _ in range(n)]
    r = ""
    z = 0
    for i in range(n):
        for j in range(n):
            if s[i] == t[j]:
                if i == 0 or j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i-1][j-1] + 1
                if l[i][j] > z and s[i-l[i][j]+1:i+1] == t[j-l[i][j]+1:j+1][::-1]:
                    z = l[i][j]
                    r = s[i-l[i][j]+1:i+1]
    return r


def longestPalindromicSubstring_dynamicProgramming(s):
    n = len(s)
    p = [[False] * n for _ in range(n)]
    r = ""
    z = 0
    for j in range(n):
        for i in range(j+1):
            if i == j or (i+1 == j and s[i] == s[j]):
                p[i][j] = True
            else:
                p[i][j] = p[i+1][j-1] and s[i] == s[j]
            if p[i][j] and j-i+1 > z:
                r = s[i:j+1]
                z = len(r)
    return r


def expandAroundCenter(s,left,right):
    n,L,R = len(s),left,right
    while L >= 0 and R < n and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1


def longestPalindromicSubstring_expandAroundCenter(s):
    if len(s) == 0:
        return s
    n = len(s)
    start,end = 0,0
    for i in range(n):
        l1 = expandAroundCenter(s,i,i)
        l2 = expandAroundCenter(s,i,i+1)
        l = max(l1,l2)
        if l > end - start:
            start = i - (l - 1) // 2
            end = i + l // 2
    return s[start:end+1]


if __name__ == "__main__":
    solutions = [
        longestPalindromicSubstring_bruteForce,
        longestPalindromicSubstring_longestCommonSubstring,
        longestPalindromicSubstring_dynamicProgramming,
        longestPalindromicSubstring_expandAroundCenter
    ]
    tests = [
        (("babad",),"bab"),
        (("cbbd",),"bb"),
        (("a",),"a"),
        (("ac",),"a"),
        (("bb",),"bb"),
        (("aacabdkacaa",),"aca")
    ]
    util.run_tests(solutions,tests,equals=lambda a,b: len(a) == len(b))
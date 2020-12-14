# https://leetcode.com/problems/longest-substring-without-repeating-characters/
import util


def longestSubstringWithoutRepeatingCharacters_bruteForce(s):
    n = len(s)
    l = 0
    for i in range(n):
        for j in range(i+1,n+1):
            if len(set(s[i:j])) == len(s[i:j]):
                l = max(l,j-i)
    return l


def longestSubstringWithoutRepeatingCharacters_slidingWindow(s):
    n = len(s)
    c = set()
    i,j,l = 0,0,0
    while i < n and j < n:
        if s[j] not in c:
            c.add(s[j])
            j += 1
            l = max(l,j-i)
        else:
            c.remove(s[i])
            i += 1
    return l


def longestSubstringWithoutRepeatingCharacters_slidingWindowOptimized(s):
    n = len(s)
    map = dict()
    i,l = 0,0
    for j in range(n):
        if s[j] in map:
            i = max(map.get(s[j]),i)
        l = max(l,j-i+1)
        map[s[j]] = j+1
    return l


if __name__ == "__main__":
    solutions = [longestSubstringWithoutRepeatingCharacters_bruteForce,longestSubstringWithoutRepeatingCharacters_slidingWindow,longestSubstringWithoutRepeatingCharacters_slidingWindowOptimized]
    tests = [
        (("abcabcbb",),3),
        (("bbbbb",),1),
        (("pwwkew",),3),
        (("",),0)
    ]
    util.run_tests(solutions,tests)
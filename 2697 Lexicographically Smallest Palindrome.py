class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        first, second = 0, len(s) - 1
        while first < second:
            if s[first] > s[second]:
                s[first] = s[second]
            else:
                s[second] = s[first]
            first += 1
            second -= 1
        return ''.join(s)


print(Solution().makeSmallestPalindrome("seven"))

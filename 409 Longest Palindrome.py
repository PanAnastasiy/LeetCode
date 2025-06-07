from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        flag = False
        c = Counter(s)
        for value in c.values():
            if not value % 2:
                answer += value
            else:
                flag = True
                answer += value - 1
        return answer + flag



print(Solution().longestPalindrome("abccccdd"))

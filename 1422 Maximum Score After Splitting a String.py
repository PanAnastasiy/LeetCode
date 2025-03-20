class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(len(s) - 1):
            left_score = s[: i + 1].count('0')
            right_score = s[i + 1:].count('1')
            if left_score + right_score > max_score:
                max_score = left_score + right_score
        return max_score


print(Solution().maxScore("011101"))
print(Solution().maxScore("00111"))
print(Solution().maxScore("00"))

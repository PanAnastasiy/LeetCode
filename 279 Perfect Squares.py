
class Solution(object):

    def numSquares(self, n):
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for j in range(1, int(n**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]


print(Solution().numSquares(36))
print(Solution().numSquares(12))
print(Solution().numSquares(13))

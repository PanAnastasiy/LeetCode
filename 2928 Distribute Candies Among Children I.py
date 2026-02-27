class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        answer = 0
        for first in range(limit + 1):
            for second in range(limit + 1):
                for third in range(limit + 1):
                    if first + second + third == n:
                        answer += 1
        return answer

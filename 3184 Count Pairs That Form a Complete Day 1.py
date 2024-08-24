class Solution(object):

    def countCompleteDayPairs(self, hours: list[int]) -> int:
        answer = 0
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if not (hours[i]+hours[j]) % 24:
                    answer += 1
        return answer


sol = Solution()
print(sol.countCompleteDayPairs([12, 12, 30, 24, 24]))

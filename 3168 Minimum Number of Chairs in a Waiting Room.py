class Solution:
    def minimumChairs(self, s: str) -> int:
        answer, total = 0, 0
        for i in s:
            if i == 'E':
                total += 1
                if total > answer:
                    answer = total
            else:
                total -= 1
        return answer


sol = Solution()
print(sol.minimumChairs("ELEELEELLL"))

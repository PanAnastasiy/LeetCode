class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        answer = []
        data = set()
        for num in nums:
            if num in data:
                answer.append(num)
            else:
                data.add(num)
            if len(answer) == 2:
                return answer


sol = Solution()
print(sol.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))

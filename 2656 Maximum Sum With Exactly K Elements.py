class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        answer = 0
        next = max(nums)
        for _ in range(k):
            answer += next
            next += 1
        return answer


print(Solution().maximizeSum([1, 2, 3, 4, 5], 3))

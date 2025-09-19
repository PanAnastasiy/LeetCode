class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        answer = []
        nums.sort(reverse=True)
        i = 0
        while len(answer) < k and i < len(nums):
            if nums[i] not in answer:
                answer.append(nums[i])
            i += 1
        return answer


print(Solution().maxKDistinct([84, 93, 100, 77, 90], 3))

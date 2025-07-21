class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    answer += 1
        return answer


print(Solution().countPairs([3, 1, 2, 2, 2, 1, 3], 2))

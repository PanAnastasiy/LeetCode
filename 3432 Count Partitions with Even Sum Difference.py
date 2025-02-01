
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if not (sum(nums[:i]) - sum(nums[i:])) % 2:
                answer += 1
        return answer


print(Solution().countPartitions([10, 10, 3, 7, 6]))
print(Solution().countPartitions([1, 2, 2]))
print(Solution().countPartitions([2, 4, 6, 8]))
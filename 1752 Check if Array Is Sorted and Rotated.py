class Solution:
    def check(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if sorted(nums) == nums:
                return True
            nums.append(nums[0])
            nums.pop(0)
        return False


print(Solution().check([3, 4, 5, 1, 2]))

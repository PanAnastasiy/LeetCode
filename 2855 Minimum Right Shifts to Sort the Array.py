class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        counter = 0
        first = nums[0]
        s = sorted(nums)
        if nums == s:
            return 0
        while nums.index(first) != len(nums) - 1 and s != nums:
            last = nums.pop()
            nums.insert(0, last)
            counter += 1
        return counter if s == nums else -1


print(Solution().minimumRightShifts([3, 4, 5, 1, 2]))

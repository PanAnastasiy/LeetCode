class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        first, second = 0, len(nums) - 1
        unique = set()
        nums.sort()
        while first < second:
            avg = (nums[first] + nums[second]) / 2
            unique.add(avg)
            first += 1
            second -= 1
        return len(unique)


print(Solution().distinctAverages([4, 1, 4, 0, 3, 5]))

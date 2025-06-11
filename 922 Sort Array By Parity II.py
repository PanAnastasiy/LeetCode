class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        first, second = 1, len(nums) // 2
        while second <= len(nums) - 1:
            nums[first], nums[second] = nums[second], nums[first]
            first += 2
            second += 2
        return nums


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
print(Solution().sortArrayByParityII([2, 3]))

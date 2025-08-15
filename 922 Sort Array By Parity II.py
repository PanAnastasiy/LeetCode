class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        nums.sort(key=lambda x: x % 2 == 0)
        first = 0
        n = len(nums)
        while first < n // 2:
            nums[first], nums[n - first - 1] = nums[n - first - 1], nums[first]
            first += 2
        return nums


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
print(Solution().sortArrayByParityII([2, 3]))
print(Solution().sortArrayByParityII([3, 7, 2, 4]))
print(Solution().sortArrayByParityII([4, 1, 2, 1]))

